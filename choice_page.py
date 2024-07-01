from sims import process_sim, data_dict
import sys
def user_choice():
    try: 
        while True:
            choice = int(input("1 to start cancellations, 2 to exit: "))
            if choice == 1:
                print(f"{data_dict}")
                process_sim(data_dict)
                break
            elif choice == 2:
                print("Exiting Program.")
                sys.exit() # Exit program
            else:
                print("Invalid Choice, please try again")

    except ValueError:
        print("Value error, use only 1 or 2")
    

