from bottle import Bottle, template, static_file, redirect, abort
from controllers.docker_controller import DockerController

server = Bottle()

docker_controller = DockerController()


@server.route('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='./static')


@server.route('/')
def home():
    return template('home', page='Home', containers=docker_controller.containers)


@server.route('/select_image')
def select_image():
    return template('select_image', page='Select Image', images=docker_controller.images)


@server.route('/create/<image_name>')
def create(image_name):
    image = docker_controller.get_image(image_name)
    if image:
        container = docker_controller.create(image)
        return template('create', page='Creating Image', container=container)
    else:
        abort(404, "Image {} not found".format(image_name))


@server.route('/state/<container_id>')
def get_state(container_id):
    return container_id
