from datetime import datetime
from typing import Optional, List

from sqlalchemy import String, Integer, Boolean, DateTime, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

# 用户-角色关联表
user_role = Table(
    "sys_user_role",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("sys_user.id"), primary_key=True),
    Column("role_id", Integer, ForeignKey("sys_role.id"), primary_key=True),
)


class SysUser(Base):
    __tablename__ = "sys_user"

    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, comment="用户名")
    password: Mapped[str] = mapped_column(String(255), nullable=False, comment="密码")
    name: Mapped[str | None] = mapped_column(String(100), nullable=True, comment="姓名")
    phone: Mapped[str | None] = mapped_column(String(20), nullable=True, comment="手机号")
    email: Mapped[str | None] = mapped_column(String(100), nullable=True, comment="邮箱")
    status: Mapped[int] = mapped_column(Integer, default=1, comment="状态 1=启用 0=禁用")
    is_deleted: Mapped[int] = mapped_column(Integer, default=0, comment="是否删除")
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True, comment="删除时间")

    # 关联关系
    roles: Mapped[List["SysRole"]] = relationship("SysRole", secondary=user_role, back_populates="users", lazy="selectin")

    def __repr__(self):
        return f"<SysUser(id={self.id}, username={self.username}, name={self.name})>"
