from bottle import Bottle, template, static_file, request, redirect
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


@server.route('/select_image')
def create():
    return template('select_image', page='Select Image')


@server.route('/configure_container', method='POST')
def configure_container():
    image = request.forms.get('image')
    return template('configure_container', page='Configure Container', image=image)


@server.route('/create', method='POST')
def create():
    name = request.forms.get('name')
    image = request.forms.get('image')
    docker_controller.run(image, name)
    return redirect('/')
