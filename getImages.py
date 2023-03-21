import base64
from flask import Flask, request, send_file
from colorCorrection import Main

app = Flask(__name__)


@app.route("/")
def index():
    return "hello"

@app.route('/api/upload', methods=['POST'])
def upload():
    # Decode the base64-encoded photo

    photo = request.files['photo']
    option = request.json['option']

    #save photo
    photo.save(photo.filename)

    # option = "Deutranopia"
    #photo = base64.b64decode(base64_photo)
    
    #IMG_DIR = photo.filename
    IMG_DIR = photo.filename


    if option == "Protanopia":
         Main.correctImage(get_path=IMG_DIR,
                            return_type_image='save',
                            save_path ='correctedImage.png',
                            degree_of_protanopia=0.9,
                            degree_of_deutranopia=0.0)
    elif option == "Deutranopia":
        Main.correctImage(get_path=IMG_DIR,
                          return_type_image='save',
                          save_path='correctedImage.png',
                          degree_of_protanopia=0.0,
                          degree_of_deutranopia=1.0)

    
    ## get conrrected image

    return send_file('correctedImage.png' , mimetype='image/png')



if __name__ == "__main__":
    app.run(debug=True , port=8000, host='0.0.0.0')