# pip install cryptography
from cryptography.fernet import Fernet   # cryptography is the package consisting of many modules; fernet is the module; Fernet is the class name.
# module is .py file, which can be imported and reused by other python files.

class PasswordManager:
    def __init__(self):
        self.key = None        # not having a key yet, but will set.
        self.password_file = None  # password_file: save encryped passwords.
        self.password_dict = {}    # password_dict: save site-password pairs. empty dictionary instead of None will be more convenient to add items immediately later.

    def create_key(self, path):     # this key used to access the password manager. path: the location or filename where the key will be stored.
        self.key = Fernet.generate_key()  # make a random 32-byte key
        with open (path, "wb") as f:   # wb: write binary mode
            f.write(self.key)          # with open will automatically generate the file if not existed, and close the file after load

    def load_key(self, path):  # read a previouly save key file and sets self.key
        with open(path, "rb") as f:  # f: a file object or a connection to a file, not the file data
            self.key = f.read()  # because f is a file object not the file data, so we need to use f.read().

    def create_password_file(self, path, initial_values = None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():  # .items() is a method of a dictionary in python, give you all key-value paris in dictionary as tuples.
                self.add_password(key, value)  # the add_password() was defined after it's used here, which is ok because python loads the whole class before using it.

    def load_password_file(self, path):
        self.password_file = path

        with open(path, "r") as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()   # save the decrypted password with the correspondin site information to key-value pair in dictionary.

    def add_password(self, site, password):   # encrypt and save the new password to dictionary
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, "a") as f:   # a: append mode
                encrypted = Fernet(self.key).encrypt(password.encode())  # password.encode(): converts the password string into bytes
                f.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        return self.password_dict[site]



def main():      # main() function: creates a small dictionary of sample passwords to test with.
    password = {
        "email": "1234567",
        "facebook": "qqisgreat",
        "youtube": "hahaisgreat"
    }

    pm = PasswordManager()  # instantiate a PasswordManager object.

    print("""What do you want to do?
        1) create a new key;
        2) load an existing key;
        3) create new password file;
        4) load existing password file;
        5) add a new password;
        6) get a password.
        7) quit
        """)

    done = False

    while not done:
        choice = input("Enter your choice: ")
        if choice == "1":
            path = input("Enter path: ")
            pm.create_key(path)
        elif choice == "2":
            path = input("Enter path: ")
            pm.load_key(path)
        elif choice == "3":
            path = input("Enter path: ")
            pm.create_password_file(path, password)
        elif choice == "4":
            path = input("Enter path: ")
            pm.load_password_file(path)
        elif choice == "5":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
        elif choice == "6":
            site = input("What site do you want: ")
            print(f"Password for {site} is {pm.get_password(site)}")
        elif choice == "q":
            done = True
            print("Bye")
        else:
            print("Invalid choice!")



if __name__ == "__main__":  # only run the following code if this file is being run directly, not imported somewhere else.
    main()
# __name__: built-in variable that stores the name of the current module
# __main__: Special value Python uses when a file is executed directly


'''
pm = PasswordManager()
pm.create_key("mykey.key")
'''
