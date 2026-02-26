import os

def _load_config_env():
    path = "config.env"
    config = {}
    if os.path.isfile(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    k, v = k.strip(), v.strip()
                    config[k] = v
                    os.environ.setdefault(k, v)
    return config

CONFIG = _load_config_env()

API_KEY = CONFIG.get("OANDA_API_KEY", os.environ.get("OANDA_API_KEY", "xxx"))
ACCOUNT_ID = CONFIG.get("OANDA_ACCOUNT_ID", os.environ.get("OANDA_ACCOUNT_ID", "xxx"))
OANDA_URL = CONFIG.get("OANDA_URL", os.environ.get("OANDA_URL", "https://api-fxpractice.oanda.com/v3"))

SECURE_HEADER = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

SELL = -1
BUY = 1
NONE = 0