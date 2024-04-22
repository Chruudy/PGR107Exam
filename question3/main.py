class Message:
    # Constructor takes sender and recipient as parameters
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.body = ""

    # Method to return the sender's name
    def get_sender(self):
        return self.sender

    # Method to return the recipient's name
    def get_recipient(self):
        return self.recipient

    # Method to append a line of text to the message body
    def append(self, text):
        self.body += text + "\n"

    # Method to convert the message into a string
    def toString(self):
        return f"From: {self.sender}\nTo: {self.recipient}\nMessage: {self.body}"

# Get sender, recipient, and message from users input
sender = input("Enter the sender's name: ")
while not sender: # Check if the sender's name is empty
    print("Sender's name cannot be empty") # Print an error message
    sender = input("Enter the sender's name: ") # Ask the user to enter the sender's name again

recipient = input("Enter the recipient's name: ")
while not recipient: # Check if the recipient's name is empty
    print("Recipient's name cannot be empty") # Print an error message
    recipient = input("Enter the recipient's name: ") # Ask the user to enter the recipient's name again

message_text = input("Enter the message: ")
while not message_text: # Check if the message is empty
    print("Message cannot be empty")  # Print an error message
    message_text = input("Enter the message: ")  # Ask the user to enter the message again

# Create a message
message = Message(sender, recipient)

# Append text to the message
message.append(message_text)

# Print the message
print(message.toString())