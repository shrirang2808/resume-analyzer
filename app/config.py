import os

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
DATA_DIR: str = os.path.join(BASE_DIR, "..", "data")

JD_PATH: str = os.path.join(DATA_DIR, "job_description", "jd.pdf")
