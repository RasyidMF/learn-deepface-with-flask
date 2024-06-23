# This API created by RasyidMF for learning purpose.
# To do more action, you can costumize this function
# 

import json
from flask import Blueprint, request, jsonify
from helper.utils import getEnv, isEmpty
from service.deepface import find
import base64

api = Blueprint("api", __name__, url_prefix="/api")
allowedImage = ["image/jpeg", "image/png", "image/jpg", "image/webp"]

@api.route("/")
def index():
    return jsonify({
        "message": "Here is your DeepFace API service",
    })
    
@api.route("/check", methods=['POST'])
def check():
    imageBase = request.form.get('image')
    imageFile = request.files.get('image')
    name = request.form.get('name')
    
    fixImageBase64 = ""
    
    if not isEmpty(imageBase):
        check = ['data:', 'image', 'base64;']
        for c in check:
            if not c in imageBase:
                return jsonify({
                    "status": 412,
                    "message": "Image is not valid"
                }), 412
        
        fixImageBase64 = imageBase
        
    if not isEmpty(imageFile):
        mimeType = imageFile.mimetype
        
        # Check if valid image
        if not mimeType in allowedImage:
            return jsonify({
                "status": 412,
                "message": "Image binary not valid"
            }), 412
        
        # Convert uploaded binary to base64
        fixImageBase64 = "data:" + mimeType + ";base64," + base64.b64encode(imageFile.read()).decode()

    if isEmpty(fixImageBase64): return jsonify({
        "status": 412,
        "message": "Image is required"
    }), 412
        
    # Execute deepface service
    try:
        result = find(
            img_path=fixImageBase64,
            path=name
        )
        
        # Check is empty
        if result[0].empty:
            return jsonify({
                "status": 200,
                "data": [],
                "message": "Can't find the simillar face with this image" 
            })
        else:
            result = json.loads(result[0].to_json())
            return jsonify({
                "status": 200,
                "data": result,
                "message": "Finded simillar face" 
            })
    
    except Exception as ex:
        return jsonify({
            "status": 500,
            "message": "Failed to check image",
            "service": ex.__str__()
        }), 500
    