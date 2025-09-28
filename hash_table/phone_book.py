#  Simple Phone Book using Python Dictionary (Hash Table)

# Initialize the phone book
phone_book = {}

# ----------------------
# Add or update a contact
def add_or_update(name, number):
    """Add a new contact or update existing contact number"""
    phone_book[name] = number
    print(f"{name} has been added/updated.")

# ----------------------
# Delete a contact
def delete_contact(name):
    """Delete a contact if it exists"""
    if name in phone_book:
        del phone_book[name]
        print(f"{name} has been deleted.")
    else:
        print(f"{name} not found.")

# ----------------------
# Search for a contact
def search_contact(name):
    """Search for a contact by name"""
    if name in phone_book:
        print(f"{name}'s number: {phone_book[name]}")
    else:
        print(f"{name} not found.")

# ----------------------
# Show all contacts
def show_all():
    """Display all contacts"""
    if phone_book:
        print("\nPhone Book:")
        for name, number in phone_book.items():
            print(name, ":", number)
    else:
        print("Phone book is empty.")

# ----------------------
# Example Usage
add_or_update("Ali", "0791234567")
add_or_update("Sara", "0789876543")
add_or_update("Omar", "0775554321")

search_contact("Sara")
search_contact("Lina")

delete_contact("Omar")
delete_contact("Lina")

add_or_update("Sara", "0781112222")  # Update existing number

show_all()
