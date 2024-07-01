from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access passwords from environment variables
PASS = os.getenv('PASSWORD1')
PASS2 = os.getenv('PASSWORD2')

if not PASS or not PASS2:
    raise ValueError("Required environment variables (PASSWORD1 or PASSWORD2) are missing.")

# Now you can use PASSWORD1 and PASSWORD2 in your code
print(f"Password 1: {PASS}")
print(f"Password 2: {PASS2}")
