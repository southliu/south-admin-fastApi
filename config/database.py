import yaml
from pathlib import Path
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

_config_path = Path(__file__).parent.parent / "config.yaml"

with open(_config_path, "r", encoding="utf-8") as f:
    _config = yaml.safe_load(f)

ASYNC_DATABASE_URL = _config["database"]["url"]

async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True,
    pool_size=20,
    max_overflow=10,
    pool_recycle=3600
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
