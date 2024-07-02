from cancel_sims import process_sim, data_dict
from suspend import suspend_sim
import sys
def user_choice():
    try: 
        while True:
            choice = int(input("1 to Cancel Sims, 2 for Suspensions, 3 to Exit:  "))
            if choice == 1:
                print(f"{data_dict}")
                process_sim(data_dict)
                break
            elif choice == 2:
                print(f"{data_dict}")
                suspend_sim(data_dict)
                break
            elif choice == 3:
                print("Exiting Program")
                sys.exit()
            else:
                print("Invalid Choice, please try again")

    except ValueError:
        print("Value error, use only 1 or 2")
    

