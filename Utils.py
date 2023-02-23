import numpy as np
import cv2
from PIL import Image

class Modify:

    def RGB_TO_LMS():

        return np.array([[17.8824, 43.5161, 4.11935],
                         [3.45565, 27.1554, 3.86714],
                         [0.0299566, 0.184309, 1.46709]])

    def LMS_TO_RGB() -> np.ndarray:

        return np.array([[0.0809, -0.1305, 0.1167],
                         [-0.0102, 0.0540, -0.1136],
                         [-0.0004, -0.0041, 0.6935]])

    def colour_correction_matrix(degree_of_protanopia, degree_of_deutranopia) -> np.ndarray:

        return np.array([[1 - degree_of_deutranopia/2, degree_of_deutranopia/2, 0],
                         [degree_of_protanopia/2, 1 - degree_of_protanopia/2, 0],
                         [degree_of_protanopia/4, degree_of_deutranopia/4, 1 - (degree_of_protanopia + degree_of_deutranopia)/4]])

class LoadImage:

    def process_RGB(path):
        rgb_image = np.array(Image.open(path)) / 255
        return rgb_image

    def process_LMS(path):
        rgb_image = np.array(Image.open(path)) / 255
        lms_image = np.dot(rgb_image[:,:,:3], Modify.rgb_to_lms())
        return lms_image
