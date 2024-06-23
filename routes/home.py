from flask import Blueprint, request, jsonify
from helper.utils import getEnv

home = Blueprint("home", __name__)

@home.route("/")
def index():
    return jsonify({
        "message": "Learn DeepFace with Flask, to access the api please check /api",
        "version": getEnv('APP_VERSION', '1.0'),
        "createdBy": "RasyidMF"
    })