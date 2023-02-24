import argparse
import os

import numpy as np
from PIL import Image
import cv2

from Utils import Modify,LoadImage

class Main:

    def correctImage(get_path:str,
                     degree_of_protanopia : float = 1.0,
                     degree_of_deutranopia : float = 1.0,
                     return_type:str = 'save',
                     save:str = None):

     rgb_image = utils.process_RGB(get_path) 
     print("hello world")              