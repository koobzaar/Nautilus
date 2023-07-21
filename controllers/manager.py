from controllers.cloud_controllers.google_cloud_controller import GoogleCloudController

class CloudManager:
    SUPPORTED_CLOUDS = {
        'google': GoogleCloudController
    }

    def __init__(self, cloud_name):
        self.cloud_name = cloud_name.lower()
        self.cloud_controller_class = self.SUPPORTED_CLOUDS.get(self.cloud_name)
        if self.cloud_controller_class is None:
            raise ValueError(f"Cloud '{self.cloud_name}' is not supported.")

    def get_cloud_controller(self):
        return self.cloud_controller_class

