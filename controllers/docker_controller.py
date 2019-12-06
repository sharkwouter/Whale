import docker
import threading


class DockerController:

    def __init__(self):
        self.__client = docker.from_env()

    def get_images(self):
        return self.__client.images.list()

    def get_containers(self):
        return self.__client.containers.list()

    def run(self, image, name):
        thread = threading.Thread(
            target=self.__create_container,
            args=(image, name)
        )
        thread.start()

    def __create_container(self, image, name):
        self.__client.containers.run(
            image,
            name=name,
            restart_policy={"Name": "always"},
            publish_all_ports=True,
        )
