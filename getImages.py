import base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload():
    # Decode the base64-encoded photo
    base64_photo = request.json['photo']
    photo = base64.b64decode(base64_photo)

    # Process the photo or save it to disk
    # ...

    return 'Photo uploaded successfully!'