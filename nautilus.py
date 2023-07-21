from adapters.cloud_adapter import CloudAdapter

class Nautilus(CloudAdapter):
    def __init__(self, cloud_controller):
        super().__init__(cloud_controller)
        

    def find_nautilus_folder(self):
        self.list_folders();