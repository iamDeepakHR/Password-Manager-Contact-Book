import json
import random
import string
import hashlib
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, email, phone):
        if name not in self.contacts:
            self.contacts[name] = {"email": email, "phone": phone}
            messagebox.showinfo("Success", f"Contact {name} added successfully!")
        else:
            messagebox.showinfo("Succes",f"Contact {name} already exists.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Succes",f"Contact {name} removed successfully!")
        else:
            messagebox.showinfo("Succes",f"Contact {name} not found.")

    def search_contact(self, name):
        if name in self.contacts:
            messagebox.showinfo("Succes",f"Name: {name}\n Email: {self.contacts[name]['email']}\nPhone: {self.contacts[name]['phone']}")
        else:
            messagebox.showinfo("Succes",f"Contact {name} not found.")

    def display_contacts(self):
        if self.contacts:
            for name, info in self.contacts.items():
                messagebox.showinfo("Succes",f"CONTACTS\nName: {name}\n Email: {info['email']}\n Phone: {info['phone']}")
        else:
            messagebox.showinfo("Succes",f"No contacts found.")

    def save_contacts(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.contacts, f)
        messagebox.showinfo("Succes",f"Contacts saved successfully.")

    def load_contacts(self, filename):
        with open(filename, 'r') as f:
            self.contacts = json.load(f)
        messagebox.showinfo("Succes",f"Contacts loaded successfully.")

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def add_password(self, domain, username, password):
        if domain not in self.passwords:
            self.passwords[domain] = {"username": username, "password": self.hash_password(password)}
            messagebox.showinfo("Succes",f"Password for {domain} added successfully!")
        else:
            messagebox.showinfo("Succes",f"Password for {domain} already exists.")

    def remove_password(self, domain):
        if domain in self.passwords:
            del self.passwords[domain]
            messagebox.showinfo("Succes",f"Password for {domain} removed successfully!")
        else:
            messagebox.showinfo("Succes",f"Password for {domain} not found.")

    def search_password(self, domain):
        if domain in self.passwords:
            messagebox.showinfo("Succes",f"Domain: {domain}\n Username: {self.passwords[domain]['username']}\n Password: {self.passwords[domain]['password']}")
        else:
            messagebox.showinfo("Succes",f"Password for {domain} not found.")

    def display_passwords(self):
        if self.passwords:
            for domain, info in self.passwords.items():
                messagebox.showinfo("Succes",f"PASSWORDS\nDomain: {domain}\n Username: {info['username']}\n Password: {info['password']}")
        else:
            messagebox.showinfo("Succes","No passwords found.")

    def save_passwords(self, filename):
        with open(filename, 'a') as f:
            json.dump(self.passwords, f)
        messagebox.showinfo("Succes",f"Passwords saved successfully.")

    def load_passwords(self, filename):
        with open(filename, 'r') as f:
            self.passwords = json.load(f)
        messagebox.showinfo("Succes",f"Passwords loaded successfully.")

def contact_menu(contact_book):
    root = tk.Tk()
    root.withdraw() # Hide the main Tkinter window

    while True:
        choice = simpledialog.askinteger("Menu", "1. Add Contact\n2. Remove Contact\n3. Search Contact\n4. Display Contacts\n5. Save Contacts\n6. Load Contacts\n7. Exit\nEnter your choice:")
        
        if choice == 1:
            name = simpledialog.askstring("Add Contact", "Enter name:")
            email = simpledialog.askstring("Add Contact", "Enter email:")
            phone = simpledialog.askstring("Add Contact", "Enter phone:")
            contact_book.add_contact(name, email, phone)
        elif choice == 2:
            name = simpledialog.askstring("Remove Contact", "Enter name:")
            contact_book.remove_contact(name)
        elif choice == 3:
            name = simpledialog.askstring("Search Contact", "Enter name:")
            contact_book.search_contact(name)
        elif choice == 4:
            contact_book.display_contacts()
        elif choice == 5:
            filename = simpledialog.askstring("Save Contacts", "Enter filename:")
            contact_book.save_contacts(filename)
        elif choice == 6:
            filename = simpledialog.askstring("Load Contacts", "Enter filename:")
            contact_book.load_contacts(filename)
        elif choice == 7:
            messagebox.showinfo("Succes","Exiting...")
            break
        else:
            messagebox.showinfo("Succes","Invalid choice. Please try again.")

def password_menu(password_manager):
    root = tk.Tk()
    root.withdraw() # Hide the main Tkinter window

    while True:
        choice = simpledialog.askinteger("Menu", "1. Generate Password\n2. Add Password\n3. Remove Password\n4. Search Password\n5. Display Passwords\n6. Save Passwords\n7. Load Passwords\n8. Exit\nEnter your choice:")
        
        if choice == 1:
            length = simpledialog.askinteger("Generate Password", "Enter length:")
            password = password_manager.generate_password(length)
            messagebox.showinfo("Succes",f"Generated Password: {password}")
        elif choice == 2:
            domain = simpledialog.askstring("Add Password", "Enter domain:")
            username = simpledialog.askstring("Add Password", "Enter username:")
            password = simpledialog.askstring("Add Password", "Enter password:")
            password_manager.add_password(domain, username, password)
        elif choice == 3:
            domain = simpledialog.askstring("Remove Password", "Enter domain:")
            password_manager.remove_password(domain)
        elif choice == 4:
            domain = simpledialog.askstring("Search Password", "Enter domain:")
            password_manager.search_password(domain)
        elif choice == 5:
            password_manager.display_passwords()
        elif choice == 6:
            filename = simpledialog.askstring("Save Passwords", "Enter filename:")
            password_manager.save_passwords(filename)
        elif choice == 7:
            filename = simpledialog.askstring("Load Passwords", "Enter filename:")
            password_manager.load_passwords(filename)
        elif choice == 8:
            messagebox.showinfo("Succes","Exiting...")
            break
        else:
            messagebox.showinfo("Succes","Invalid choice. Please try again.")

def main():
    while True:
        choice = simpledialog.askinteger("Menu", "1.Contact Book \n2. Password Manager\n3. Exit")
        if choice == 1:
            contact_menu(ContactBook())
        elif choice == 2:
            password_menu(PasswordManager())
        elif choice == 3:
            messagebox.showinfo("Succes","Exiting...")
            break
        else:
            messagebox.showinfo("Succes","Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
