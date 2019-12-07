from config import Config


class Image:

    def __init__(self, image_dict):
        self.name = image_dict['name']
        self.description = image_dict['description']
        self.container = image_dict['container']
        self.volumes = image_dict['volumes']
        if image_dict['requires_database']:
            self.database_type = image_dict['database_type']

        self.__docker_client = Config.docker_client

        self.installed = False

    def pull(self):
        self.__docker_client.pull_image(self.container)

    def __str__(self):
        return self.name

    def __lt__(self, other):
        names = [str(self), str(other)]
        names.sort()
        if names[0] == str(self):
            return True
        return False
