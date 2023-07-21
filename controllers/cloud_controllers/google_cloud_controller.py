from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class GoogleCloudController:
    def __init__(self):
        self.gauth = GoogleAuth()
        self.gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gauth)

    def upload_file(self, file_path, file_name):
        file = self.drive.CreateFile({'title': file_name})
        file.SetContentFile(file_path)
        file.Upload()
        return file['id']
    
    def list_folders(self):
        file_list = self.drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        for file in file_list:
            print('title: %s, id: %s' % (file['title'], file['id']))
    
    def create_folder(self, folder_name):
        folder = self.drive.CreateFile({'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'})
        folder.Upload()
        return folder['id']
    
    def upload_folder_to_specific_directory(self, folder_path, folder_name, parent_folder_id):
        folder_id = self.create_folder(folder_name)
        self.upload_folder(folder_path, folder_id)
        self.move_folder(folder_id, parent_folder_id)