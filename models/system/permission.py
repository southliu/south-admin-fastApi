from datetime import datetime
from typing import List

from sqlalchemy import String, Integer, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class SysPermission(Base):
    __tablename__ = "sys_permission"

    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, comment="权限名称")
    description: Mapped[str | None] = mapped_column(Text, nullable=True, comment="描述")
    is_deleted: Mapped[int] = mapped_column(Integer, default=0, comment="是否删除")
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True, comment="删除时间")

    # 关联关系
    menus: Mapped[List["SysMenu"]] = relationship("SysMenu", back_populates="permission", lazy="selectin")
    roles: Mapped[List["SysRole"]] = relationship("SysRole", secondary="sys_role_permission", back_populates="permissions", lazy="selectin")

    def __repr__(self):
        return f"<SysPermission(id={self.id}, name={self.name})>"
