import csv
import sys
from email_util import send_email


# Initialize an empty dictionary to store the data
data_dict_2 = {}

# Open the CSV file
with open('suspend-sim.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # Iterate through each row in the CSV file
    for row in reader:
        name = row[0].strip()  # Get the name (first column)
        number = row[1].strip()  # Get the number (second column)
        sim_type = row[2].strip()  # Get the sim_type (third column)
        sim_status = row[3].strip()
        account_note = row[4].strip()
        
        # Store the data in the dictionary, [name] as key, tuple (number, sim_type) as value
        data_dict_2[name] = (number, sim_type, sim_status, account_note)

def update_account_suspend(file_name, data_dict_2):
     with open(file_name, 'w', newline='') as csvfile:
          writer = csv.writer(csvfile)
          writer.writerow(['Account_Name', 'Sim_Number', 'Sim_Type', 'Sim_Status', 'account_note'])

          for name, (number, sim_type, sim_status, account_note) in data_dict_2.items():
               writer.writerow([name, number, sim_type, sim_status, account_note])


# Accessing a specific number by name
def suspend_sim(data_dict_2):
    try:
        while True:
            desired_name = input("Sonar Account (Type 'Exit' to quit): ").strip()
            if desired_name.lower() == 'exit':
                print("Exiting")
                sys.exit()
            
            if desired_name in data_dict_2:
                number, sim_type, sim_status, account_note = data_dict_2[desired_name]
                print(f"Sim card assigned to {desired_name} is {number} and the sim type is {sim_type}")
                
                if account_note == '#':
                    new_account_note = 'Sim Suspended'
                else:
                    new_account_note = account_note  # Keep the original note if condition not met
                
                # Update the dictionary
                data_dict_2[desired_name] = (number, sim_type, sim_status, new_account_note)
                update_account_suspend('suspend-sim.csv', data_dict_2)
                print(f"Note sucessfully added to {desired_name}")

                if sim_type == "Three":
                    subject = 'Suspend Sims'
                    body = f'Please set the below sim to suspend immediately:\n - {number}'
                    sender = 'luke.dowling@regionalbroadband.ie'
                    recipients = [sender, 'luke.dowling@regionalbroadband.ie']
                    send_email(subject, body, sender, recipients)
                    print("Email sent successfully for 'Three' sim type.")
                    continue

                elif sim_type == 'Eir':
                    subject = 'Cancel Sim'
                    body = f'Please set the below sim to cancel with 30 days:\n - {number}'
                    sender = 'luke.dowling@regionalbroadband.ie'
                    recipients = [sender, 'luke.dowling@regionalbroadband.ie'] 
                    send_email(subject, body, sender, recipients)
                    print("Email sent successfully for 'Eir' sim type.")
                    continue

            else:
                print("No sonar account found, try again")
                print("Available accounts:", list(data_dict_2.keys()))  # Debugging output

    except ValueError as ve:
        print(f"Value error, use only string: {ve}")
