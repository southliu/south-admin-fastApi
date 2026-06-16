from typing import Optional, List

from sqlalchemy import select, func, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models.system.menu import SysMenu
from models.system.permission import SysPermission
from schemas.menu import CreateMenuRequest, UpdateMenuRequest, ChangeMenuStateRequest


async def get_menu_by_id(db: AsyncSession, menu_id: int) -> Optional[SysMenu]:
    """根据ID查询菜单"""
    result = await db.execute(
        select(SysMenu)
        .where(and_(SysMenu.id == menu_id, SysMenu.is_deleted == 0))
        .options(selectinload(SysMenu.permission))
        .options(selectinload(SysMenu.children))
    )
    return result.scalar_one_or_none()


async def get_menu_list(db: AsyncSession, user_id: int) -> List[dict]:
    """获取用户菜单列表"""
    from crud.user import get_user_by_id

    user = await get_user_by_id(db, user_id)
    if not user:
        return []

    # 获取用户所有角色的菜单ID
    menu_ids = set()
    for role in user.roles:
        for menu in role.menus:
            menu_ids.add(menu.id)

    if not menu_ids:
        return []

    # 查询所有相关菜单
    result = await db.execute(
        select(SysMenu)
        .where(and_(SysMenu.id.in_(menu_ids), SysMenu.is_deleted == 0, SysMenu.state == 1))
        .options(selectinload(SysMenu.permission))
        .options(selectinload(SysMenu.children))
        .order_by(SysMenu.order)
    )
    menus = result.scalars().all()

    # 构建树形结构
    return build_menu_tree(menus, None)


async def get_menu_page(
    db: AsyncSession,
    page: int = 1,
    page_size: int = 10,
    label: Optional[str] = None,
    label_en: Optional[str] = None,
    state: Optional[int] = None,
    rule: Optional[str] = None
) -> dict:
    """获取菜单分页列表"""
    query = select(SysMenu).where(SysMenu.is_deleted == 0)

    if label:
        query = query.where(SysMenu.label.like(f"%{label}%"))
    if label_en:
        query = query.where(SysMenu.label_en.like(f"%{label_en}%"))
    if state is not None:
        query = query.where(SysMenu.state == state)
    if rule:
        query = query.where(SysMenu.rule.like(f"%{rule}%"))

    # 查询总数
    count_query = select(func.count()).select_from(query.subquery())
    total_result = await db.execute(count_query)
    total = total_result.scalar()

    # 分页查询
    offset = (page - 1) * page_size
    query = query.options(selectinload(SysMenu.permission)).offset(offset).limit(page_size).order_by(SysMenu.order)
    result = await db.execute(query)
    menus = result.scalars().all()

    # 构建返回数据
    items = []
    for menu in menus:
        items.append({
            "id": menu.id,
            "label": menu.label,
            "labelEn": menu.label_en,
            "icon": menu.icon,
            "type": menu.type,
            "router": menu.router,
            "rule": menu.rule,
            "order": menu.order,
            "state": menu.state,
            "parentId": menu.parent_id,
            "permissionId": menu.permission_id,
            "createdAt": menu.create_at,
            "updatedAt": menu.update_at,
        })

    total_pages = total // page_size
    if total % page_size > 0:
        total_pages += 1

    return {
        "items": items,
        "page": page,
        "pageSize": page_size,
        "total": total,
        "totalPages": total_pages,
    }


async def get_menu_detail(db: AsyncSession, menu_id: int) -> dict:
    """获取菜单详情"""
    menu = await get_menu_by_id(db, menu_id)
    if not menu:
        raise ValueError("菜单不存在")

    return {
        "id": menu.id,
        "label": menu.label,
        "labelEn": menu.label_en,
        "icon": menu.icon,
        "type": menu.type,
        "router": menu.router,
        "rule": menu.rule,
        "order": menu.order,
        "state": menu.state,
        "parentId": menu.parent_id,
        "permissionId": menu.permission_id,
        "createdAt": menu.create_at,
        "updatedAt": menu.update_at,
    }


async def create_menu(db: AsyncSession, data: CreateMenuRequest, user_id: int) -> SysMenu:
    """创建菜单"""
    menu = SysMenu(
        label=data.label,
        label_en=data.label_en,
        type=data.type,
        icon=data.icon,
        router=data.router,
        rule=data.rule,
        order=data.order,
        state=data.state,
        parent_id=data.parent_id,
    )

    db.add(menu)
    await db.commit()
    await db.refresh(menu)
    return menu


async def update_menu(db: AsyncSession, menu_id: int, data: UpdateMenuRequest) -> SysMenu:
    """更新菜单"""
    menu = await get_menu_by_id(db, menu_id)
    if not menu:
        raise ValueError("菜单不存在")

    menu.label = data.label
    menu.label_en = data.label_en
    if data.type is not None:
        menu.type = data.type
    if data.icon is not None:
        menu.icon = data.icon
    if data.router is not None:
        menu.router = data.router
    if data.rule is not None:
        menu.rule = data.rule
    if data.order is not None:
        menu.order = data.order
    if data.state is not None:
        menu.state = data.state
    if data.parent_id is not None:
        menu.parent_id = data.parent_id

    await db.commit()
    await db.refresh(menu)
    return menu


async def delete_menu(db: AsyncSession, menu_id: int) -> None:
    """删除菜单"""
    menu = await get_menu_by_id(db, menu_id)
    if not menu:
        raise ValueError("菜单不存在")

    from datetime import datetime
    menu.is_deleted = 1
    menu.deleted_at = datetime.now()
    await db.commit()


async def batch_delete_menu(db: AsyncSession, menu_ids: List[int]) -> None:
    """批量删除菜单"""
    from datetime import datetime

    for menu_id in menu_ids:
        menu = await get_menu_by_id(db, menu_id)
        if menu:
            menu.is_deleted = 1
            menu.deleted_at = datetime.now()

    await db.commit()


async def change_menu_state(db: AsyncSession, data: ChangeMenuStateRequest) -> None:
    """修改菜单状态"""
    menu = await get_menu_by_id(db, data.id)
    if not menu:
        raise ValueError("菜单不存在")

    menu.state = data.state
    await db.commit()


def build_menu_tree(menus: List[SysMenu], parent_id: Optional[int]) -> List[dict]:
    """构建菜单树形结构"""
    tree = []
    for menu in menus:
        if menu.parent_id == parent_id:
            node = {
                "id": menu.id,
                "label": menu.label,
                "labelEn": menu.label_en,
                "title": menu.label,
                "titleEn": menu.label_en,
                "key": str(menu.id),
                "value": str(menu.id),
                "icon": menu.icon,
                "type": menu.type,
                "router": menu.router,
                "rule": menu.rule,
                "order": menu.order,
                "state": menu.state,
                "parentId": menu.parent_id,
                "permissionId": menu.permission_id,
                "createdAt": menu.create_at,
                "updatedAt": menu.update_at,
                "children": build_menu_tree(menus, menu.id),
            }
            tree.append(node)
    return tree
