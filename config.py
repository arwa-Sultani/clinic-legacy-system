import os

class Config:
    DEBUG = os.getenv("DEBUG", "True") == "True"
    SECRET_KEY = os.getenv("SECRET_KEY", "devkey")
    # Add DB settings if you later switch from in-memory