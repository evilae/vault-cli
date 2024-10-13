
import os
import toml
import time

def password1():

    config = {
    'Password': {
        'Password': None, 
    }
}

    while True:
        print("Select operation.")
        print("1. Change the password ")
        print("2. Select file")
        print("3. Execute file")
        print("4. List saved files")
        print("5. Exit")  

        choice = input("")
        config_file_path = '/home/evilae/.config/config.toml' # I'll will change that at some point
                
        if choice == '1': 
                if os.path.exists(config_file_path):
                    config_reload = toml.load(config_file_path)
            new_password = input("What should the password be? ")
            config['Password']['Password'] = new_password
            with open(config_file_path, 'w') as config_file:
                toml.dump(config, config_file)
            print("Password was saved!")
            continue

        elif choice == '2':        
            file = input("Which file would you want to put in the 'safe'? ")
            if not os.path.exists(file):
                print("File was not found!")
                continue 
            else:
                print(f"The file {file} was found!")
                continue

            file_extension = input("Specify the file extension (.mp3, .mp4, .png etc): ")
            allowed_extensions = [".mp4", ".mp3", ".jpeg", ".png", ".jpg", ".gif", ".webp", ".mkv", ".avi", ".mov"]
            if file_extension in allowed_extensions:
                print(f"File extension {file_extension} is allowed!")
                print("Your file was saved in the vault")
                continue
            else: 
                print(f"The file extension {file_extension} is not allowed!")
                print("The file was not saved!")
                continue
        elif choice == '4':
            print("do something idk")

        elif choice == '5':
            if file:  
                print(f"Executing file: {file}")
                os.system(f"mpv {file}")  
                print("File was executed!")
                continue
            else:
                print("No file selected!")
                continue
        elif choice == '6':
            print("Exiting.")
            break 
        else:
            print("Invalid choice. Please try again.")

password1()
