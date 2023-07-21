from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class GoogleCloudController:
    def __init__(self):
        self.gauth = GoogleAuth()
        self.gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gauth)

    def create_folder(self, folder_name):
        folder = self.drive.CreateFile({'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'})
        folder.Upload()
        return folder['id']

    def upload_file(self, file_path, file_name):
        file = self.drive.CreateFile({'title': file_name})
        file.SetContentFile(file_path)
        file.Upload()
        return file['id']
        
    def upload_folder_to_specific_directory(self, folder_path, folder_name, parent_folder_id):
        folder_id = self.create_folder(folder_name)
        self.upload_folder(folder_path, folder_id)
        self.move_folder(folder_id, parent_folder_id)
    
    def list_folders(self):
        file_list = self.drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        # create a json of all files and parents and return
        return file_list
    
    def find_folder(self, folder_name):
        file_list = self.drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        for file in file_list:
            if file['title'] == folder_name:
                return file['id']
        return None
    
    def remove_folder(self, folder_id):
        folder = self.drive.CreateFile({'id': folder_id})
        folder.Delete()
    
    def move_folder(self, folder_id, parent_folder_id):
        folder = self.drive.CreateFile({'id': folder_id})
        folder['parents'] = [{'id': parent_folder_id}]
        folder.Upload()

    def remove_folder(self, folder_id):
        folder = self.drive.CreateFile({'id': folder_id})
        folder.Delete()
        # searches for the folder id, if it exists, return error, else return sucess
        
        
