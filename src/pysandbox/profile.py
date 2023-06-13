import os
from dotenv import load_dotenv

# load ENV variables using load_dotenv()
load_dotenv()

profile = os.getenv("APP_PROFILE")
print(f"the Python app is for '{profile}'")
