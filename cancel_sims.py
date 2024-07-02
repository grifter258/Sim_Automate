import csv
from email_util import send_email

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
        # Store the data in the dictionary
        data_dict[name] = (number, sim_type, sim_status)

# Function to process SIM data
def process_sim(data_dict):
    try:
        while True:
            desired_name = input("Sonar Account: ").strip()
            if desired_name in data_dict:
                number, sim_type, sim_status = data_dict[desired_name]
                print(f"Sim card assigned to {desired_name} is {number} and the sim type is {sim_type}, the status of this sim is {sim_status}")

                if sim_status == 'Unconsumed':
                    new_sim_status = 'Consumed'
                    
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
                    
                    # Update the status in the dictionary
                    data_dict[desired_name] = (number, sim_type, new_sim_status)
                else:
                    print(f"Sim status for {desired_name} is already {sim_status}. No action taken.")
            else:
                print("No sonar account found, try again")
    except ValueError:
        print("Value error, use only string")