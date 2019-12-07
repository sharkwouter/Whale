import json
import threading
from models import Image, Container
from config import Config


class DockerController:

    def __init__(self):
        self.client = Config.docker_client
        self.containers = self.__get_containers()
        self.installed = []
        self.images = self.__get_images()

    def __get_images(self):
        images = []
        with open('data/supported_containers.json', 'r') as file:
            data = file.read()
            file.close()
        for image_dict in json.loads(data)['images']:
            if image_dict['name'] not in self.installed:
                images.append(Image(image_dict))
        return images

    def __get_containers(self):
        containers = []
        for entry in self.client.containers.list():
            print(entry)
        return containers

    def get_image_by_container(self, container):
        for image in self.images:
            if container and image.container == container:
                return image
        return None

    def get_image(self, name):
        for image in self.images:
            if name and image.name == name:
                return image
        return None

    def create(self, image):
        thread = threading.Thread(
            target=self.__create_container,
            args=(image.name, image.container)
        )
        thread.start()

    def __create_container(self, name, container):
        self.client.containers.run(
            container,
            name=name,
            restart_policy={"Name": "always"},
            publish_all_ports=True,
        )
