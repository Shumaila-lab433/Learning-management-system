
from pathlib import Path

# Main project folder
BASE_DIR = Path(__file__).resolve().parent

# Database location
DATABASE = BASE_DIR / "results.db"

# Flask security key (development only)
SECRET_KEY = "dev-key-change-this-later"
