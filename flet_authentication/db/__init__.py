import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
db_name = "db_system.db"
db_path = os.path.join(BASE_DIR, db_name)

# if __name__ == "__main__":
#     print(db_path)
