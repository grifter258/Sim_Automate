from choice_page import user_choice
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

passw = os.getenv("email_password")

print(os.getenv("email_password"))

def main():
    user_choice()
    
if __name__ == "__main__":
    main()
