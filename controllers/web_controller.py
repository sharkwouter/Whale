from bottle import Bottle, template, static_file
from controllers.docker_controller import DockerController

server = Bottle()

docker_controller = DockerController()


@server.route('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='./static')


@server.route('/')
def home():
    containers = docker_controller.get_containers()
    return template('home', page='Home', containers=containers)


@server.route('/create')
def create():
    return template('create', page='Create')
