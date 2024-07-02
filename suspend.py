import csv
import sys
from email_util import send_email

# Initialize an empty dictionary to store the data
data_dict = {}

# Open the CSV file
with open('testsims1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # Iterate through each row in the CSV file
    for row in reader:
        name = row[0].strip()  # Get the name (first column)
        number = row[1].strip()  # Get the number (second column)
        sim_type = row[2].strip()  # Get the sim_type (third column)
        
        # Store the data in the dictionary, [name] as key, tuple (number, sim_type) as value
        data_dict[name] = (number, sim_type)

# Print the dictionary to verify
# print(f"{data_dict}")

# Accessing a specific number by name
def suspend_sim(data_dict):
    try:
        while True:
            desired_name = input(f"Sonar Account: " "Exit to quit to menu: ").strip()
            if desired_name in data_dict:
                number, sim_type = data_dict[desired_name]
                print(f"Sim card assigned to {desired_name} is {number} and the sim type is {sim_type}")
                
                if sim_type == "Three" or sim_type == 'Eir':
                    subject = 'Suspend Sims'
                    body = f'Please set the below sim to suspend immediately:\n - {number}'
                    sender = 'luke.dowling@regionalbroadband.ie'
                    recipients = [sender, 'luke.dowling@regionalbroadband.ie']
                    send_email(subject, body, sender, recipients)
                    print("Email sent successfully for 'Three' sim type.")
                    continue
            elif desired_name == 'Exit':
                print("Exiting")
                sys.exit()
            else:
                print("No sonar account found, try again")
    except ValueError:
        print("Value error, use only string")