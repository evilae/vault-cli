import os
import toml
import time

def password1():

    config = {
    'Password': {
        'Password': None, 
    },
    'Files': {
        'File Locations': []
    }
}

    while True:
        print("Select operation.")
        print("1. Change the password ")
        print("2. Select file")
        print("3. Remove file")
        print("4. List saved files")
        print("5. Execute file") 
        print("6. Exit") 

        choice = input("")
        config_file_path = '/home/evilae/.config/config.toml' # I'll will change that at some point
                
        if choice == '1': 
            if config_file_path is None:
                print("Please select a config file location first.")
                continue

                if os.path.exists(config_file_path):
                    config_reload = toml.load(config_file_path)
            new_password = input("What should the password be? ")
            config['Password']['Password'] = new_password
            with open(config_file_path, 'w') as config_file:
                toml.dump(config, config_file)
            print("Password was saved!")
            continue

        elif choice == '2':
            config = toml.load(config_file_path)
            file_path = input("Which file would you want to put in the 'safe'? ")
            if not os.path.exists(file_path):
                print("File was not found!")
                continue 
            else:
                print(f"The file {file_path} was found!")
            allowed_extensions = [".mp4", ".mp3", ".jpeg", ".png", ".jpg", ".gif", ".webp", ".mkv", ".avi", ".mov"]
            file_extension = input("Specify the file extension (.mp3, .mp4, .png etc): ")
            if file_extension in allowed_extensions:
                toml.load(config_file_path)
                print(f"File extension {file_extension} is allowed!")
                if 'File Locations' not in config['Files']:
                    config['Files']['File Locations'] = []
                config['Files']['File Locations'].append(file_path)
                with open(config_file_path, 'w') as config_file:
                    toml.dump(config, config_file)
                print(f"File was saved!")
            else:
                print(f"File path is either invalid or {file_extension} is not allowed! Please provide a valid path / valid file extension ")
                print("The file was not saved!")
                continue

        elif choice == '3':
            print("do another something idk")

        elif choice == '4':
            print("do something idk")

        elif choice == '5':
            with open(f'{config_file_path}', 'r') as config_file:
                config = toml.load(config_file)
            password_check = input("What's the password? ")
            config_password = config.get('Password', {}).get ('Password')
            if password_check == config_password:
                file_path = input("Which file would you like to execute? ")
                file_split, file_extension_5 = os.path.splitext(file_path)        
                if file_path:
                    if file_path in config.get('Files', {}).get('File Locations', []):
                        if file_extension_5 in [".jpeg", ".png", ".jpg", ".webp"]:
                            print(f"Executing file (feh): {file_path}")
                            os.system(f"feh {file_path}")
                            print("File was executed")
                        else:
                            print(f"Executing file: {file_path}") 
                            os.system(f"mpv {file_path}")
                            print("File was executed!")
                continue
            else:
                print("No file selected / password is incorrect!")
                continue
        elif choice == '6':
            print("Exiting.")
            break 
        else:
            print("Invalid choice. Please try again.")

password1()
