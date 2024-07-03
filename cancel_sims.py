import csv
from email_util import send_email
import sys
# Initialize an empty dictionary to store the data
data_dict = {}

# Open the CSV file and read the data
with open('testsims1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    # header = next(reader)  # Skip the header row if there is one
    for row in reader:
        name = row[0].strip()  # Get the name (first column)
        number = row[1].strip()  # Get the number (second column)
        sim_type = row[2].strip()  # Get the sim_type (third column)
        sim_status = row[3].strip()  # Get the sim_status (fourth column)
        account_note = row[4].strip()
        # Store the data in the dictionary
        data_dict[name] = (number, sim_type, sim_status, account_note)

def update_account_cancel(file_name, data_dict):
     with open(file_name, 'w', newline='') as csvfile:
          writer = csv.writer(csvfile)
          writer.writerow(['Account_Name', 'Sim_Number', 'Sim_Type', 'Sim_Status', 'account_note'])

          for name, (number, sim_type, sim_status, account_note) in data_dict.items():
               writer.writerow([name, number, sim_type, sim_status, account_note])

        

# print(data_dict)
# Function to process SIM data
def process_sim(data_dict):
    try:
        while True:
            desired_name = input("Sonar Account: ").strip()
            if desired_name.lower() == 'exit':
                 print("Exiting")
                 sys.exit()

            if desired_name in data_dict:
                number, sim_type, sim_status, account_note = data_dict[desired_name]
                print(f"Sim card assigned to {desired_name} is {number} and the sim type is {sim_type}, the status of this sim is {sim_status}")

                if sim_status == 'Unconsumed' and account_note == "#":
                     new_sim_status = 'Consumed'
                     new_account_note = 'Sim Cancelled'
                
                # Update the CSV File
                data_dict[desired_name] = (number, sim_type, new_sim_status, new_account_note)
                update_account_cancel('testsims1.csv', data_dict)

                if sim_type == "Three":
                        subject = 'Cancel Sim'
                        body = f'Please set the below sim to cancel with 30 days:\n - {number}'
                        sender = 'luke.dowling@regionalbroadband.ie'
                        recipients = [sender, 'luke.dowling@regionalbroadband.ie'] 
                        send_email(subject, body, sender, recipients)
                        print("Email sent successfully for 'Three' sim type.")
                    
                elif sim_type == 'Eir':
                        subject = 'Cancel Sim'
                        body = f'Please set the below sim to cancel with 30 days:\n - {number}'
                        sender = 'luke.dowling@regionalbroadband.ie'
                        recipients = [sender, 'luke.dowling@regionalbroadband.ie'] 
                        send_email(subject, body, sender, recipients)
                        print("Email sent successfully for 'Eir' sim type.")
                     
            else:
                print("No sonar account found, try again")
                print("Available accounts:", list(data_dict.keys()))
    except ValueError:
        print("Value error, use only string")
