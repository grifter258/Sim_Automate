from cancel_sims import process_sim, data_dict
from suspend import suspend_sim, data_dict_2
import sys
from pprint import pprint 
def user_choice():
    try: 
        while True:
            choice = int(input("1 to Cancel Sims, 2 for Suspensions, 3 to Exit:  "))
            if choice == 1:
                pprint(data_dict)
                process_sim(data_dict)
                break
            elif choice == 2:
                pprint(data_dict_2)
                suspend_sim(data_dict_2)
                break
            elif choice == 3:
                print("Exiting Program")
                sys.exit()
            else:
                print("Invalid Choice, please try again")

    except ValueError:
        print("Value error, use only 1 or 2")
    

