import json

def main():
    
    with open("/home/hp/Skillohomework/homework_5/homework9/contacts.json", "r") as file:
        contacts = json.load(file)

    
    print("Contact Information:")
    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Email: {contact['email']}")
        print(f"Phone: {contact['phone']}")
        print()

if __name__ == "__main__":
    main()
