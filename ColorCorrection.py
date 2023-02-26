import argparse
import os

import numpy as np
from PIL import Image
import cv2

from Utils import Modify,LoadImage

class Main:


    @staticmethod
    def correctImage(get_path:str,
                     degree_of_protanopia : float = 1.0,
                     degree_of_deutranopia : float = 1.0,
                     return_type:str = 'save',
                     save:str = None):
      #Loading the image file in LMS colour space. 
     rgb_image = LoadImage.process_RGB(get_path)

     modify = Modify.colour_correction_matrix(degree_of_deutranopia = degree_of_deutranopia,
                                              degree_of_protanopia = degree_of_protanopia) 
     
     corrected_image = np.uint8(np.dot(rgb_image,modify)*255)

     if return_type == 'PIL':
        return Image.fromarray(corrected_image)
     
     if return_type == 'np':
        return corrected_image

     if return_type == 'save':
        assert save is not None , 'Save path is not provided for image!'
        cv2.imwrite(corrected_image,save)
        return
     
   # Irushi Perera w1867413
   
     
    
    


    
               