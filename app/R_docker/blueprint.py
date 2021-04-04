#a primeira coisa é importar o blue
from flask import Blueprint, render_template

#determinar a url
docker_routes = Blueprint("docker", __name__, url_prefix="/docker")

@docker_routes.route("")
def index():
    return render_template("docker.html")