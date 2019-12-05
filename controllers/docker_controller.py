import docker


class DockerController:

    def __init__(self):
        self.client = docker.from_env()

    def get_images(self):
        return self.client.images.list()

    def get_containers(self):
        return self.client.containers.list()
