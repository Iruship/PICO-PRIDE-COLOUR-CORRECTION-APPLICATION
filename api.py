from flask import Flask, render_template, Response 

import cv2
import numpy as np

app = Flask(__name__)  

@app.route("/")
def index():
    return render_template("")



if __name__ == "__main__":
    app.run(debug=True)