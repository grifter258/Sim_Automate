import csv
from email_util import send_email

# Initialize an empty dictionary to store the data
data_dict = {}

# Open the CSV file
with open('testsims1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # Iterate through each row in the CSV file
    for row in reader:
        # Assuming each row has two columns: name and number
        name = row[0].strip()  # Get the name (first column)
        number = row[1].strip()  # Get the number (second column)
        
        # Store the data in the dictionary, [name] as key, number as value
        data_dict[name] = number

# Print the dictionary to verify
print(f"{data_dict}")

# Accessing a specific number by name
try:
    while True:
        desired_name = input("Sonar Account: ")
        if desired_name in data_dict:
                print(f"Sim card assigned to {desired_name} is {data_dict[desired_name]}") # finds Name in dictionary [the key] and return the sim number [value]

                # Email to send if the sim card is found:
                subject = 'Cancel Sim'
                body = f'Please set the below sim to cancel with 30 days:\n\n{desired_name} - {data_dict[desired_name]}'
                sender = 'sonartestsims@gmail.com'
                recipients = [sender, 'sonartestsims@gmail.com']

                # Email send
                send_email(subject, body, sender, recipients)

                break

        else:
             print("No sonar account found, try again")
except ValueError:
     print("Value error, use only string")



