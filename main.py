from controllers.manager import CloudManager
from nautilus import Nautilus
import os

def main():
        # Check if settings file exists
    if os.path.exists("settings.txt"):
        with open("settings.txt", "r") as f:
            previous_cloud_provider = f.read().strip()
    else:
        previous_cloud_provider = None

    # Ask user for cloud provider if not found in settings file
    if previous_cloud_provider is None:
        user_chosen_cloud = input("Enter the cloud provider (google/onedrive/dropbox): ")
        with open("settings.txt", "w") as f:
            f.write(user_chosen_cloud)
    else:
        user_chosen_cloud = previous_cloud_provider

    print(f"Using {user_chosen_cloud} as the cloud provider.")
    
    try:
        # Get the appropriate cloud controller class based on the user's input
        print(user_chosen_cloud)
        cloud_manager = CloudManager(user_chosen_cloud)
        cloud_controller = cloud_manager.get_cloud_controller()
        # Now, you can create an instance of the chosen cloud controller and use it as needed
        nautilus = Nautilus(cloud_controller)
        nautilus.find_nautilus_folder()


    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
