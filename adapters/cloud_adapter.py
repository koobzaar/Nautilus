class CloudAdapter:
    def __init__(self, cloud_controller_class):
        print("Cloud Adapter created")
        self.cloud = cloud_controller_class()
    
    def create_folder(self, folder_name):
        return self.cloud.create_folder(folder_name)
    
    def list_folders(self):
        return self.cloud.list_folders()
    
    def find_folder_id(self, folder_name):
        return self.cloud.find_folder(folder_name)
    
    def move_folder(self, folder_id, parent_folder_id):
        self.cloud.move_folder(folder_id, parent_folder_id)
    
    def remove_folder(self, folder_id):
        self.cloud.remove_folder(folder_id)
