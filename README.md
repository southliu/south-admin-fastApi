# South Admin FastAPI

South Admin FastAPI 后台管理系统，基于 FastAPI + SQLAlchemy + MySQL。

## 项目结构

```
south-admin-fastApi/
├── api/
│   └── routes/
│       └── system/
│           ├── user.py          # 用户接口
│           ├── role.py          # 角色接口
│           ├── menu.py          # 菜单接口
│           ├── permission.py    # 权限接口
│           └── log.py           # 日志接口
├── config/
│   ├── database.py              # 数据库配置
│   └── settings.py              # 应用配置
├── core/
│   ├── database.py              # 数据库初始化
│   └── router.py                # 路由注册
├── crud/
│   ├── user.py                  # 用户 CRUD
│   ├── role.py                  # 角色 CRUD
│   ├── menu.py                  # 菜单 CRUD
│   ├── permission.py            # 权限 CRUD
│   └── log.py                   # 日志 CRUD
├── middleware/
│   └── auth.py                  # JWT 认证中间件
├── models/
│   ├── base.py                  # 基础模型
│   └── system/
│       ├── user.py              # 用户模型
│       ├── role.py              # 角色模型
│       ├── menu.py              # 菜单模型
│       ├── permission.py        # 权限模型
│       └── log.py               # 日志模型
├── schemas/
│   ├── response.py              # 响应模型
│   ├── user.py                  # 用户 Schema
│   ├── role.py                  # 角色 Schema
│   ├── menu.py                  # 菜单 Schema
│   ├── permission.py            # 权限 Schema
│   └── log.py                   # 日志 Schema
├── utils/
│   └── security.py              # 安全工具
├── main.py                      # 应用入口
├── pyproject.toml               # 项目配置
├── config.yaml                  # 应用配置（不入库）
└── config.yaml.example          # 配置文件示例
```

## 快速开始

### 1. 安装依赖

```bash
pip install uv
uv sync
```

### 2. 配置应用

复制 `config.yaml.example` 为 `config.yaml`，并修改数据库和 JWT 配置：

```bash
cp config.yaml.example config.yaml
```

配置文件格式：

```yaml
database:
  url: "mysql+aiomysql://root:your_password@localhost:3306/south_admin?charset=utf8mb4"

jwt:
  secret_key: "your-secret-key-here"
  algorithm: "HS256"
  access_token_expire_minutes: 1440
```

### 3. 启动服务

```bash
uv run uvicorn main:app --reload
```

### 4. 导入数据库数据

```bash
docker cp database/init.sql admin:/tmp/init.sql
docker exec admin bash -c "mysql -u root -p'your_password' --default-character-set=utf8mb4 south_admin < /tmp/init.sql"
```

### 5. 访问 API 文档

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 认证方式

使用 JWT Bearer Token 认证，在请求头中添加：

```
Authorization: Bearer <token>
```
