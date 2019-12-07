import docker


class Config:
    docker_client = docker.from_env()
