import yaml
from pathlib import Path

_config_path = Path(__file__).parent.parent / "config.yaml"

with open(_config_path, "r", encoding="utf-8") as f:
    _config = yaml.safe_load(f)

SECRET_KEY = _config["jwt"]["secret_key"]
ALGORITHM = _config["jwt"]["algorithm"]
ACCESS_TOKEN_EXPIRE_MINUTES = _config["jwt"]["access_token_expire_minutes"]
