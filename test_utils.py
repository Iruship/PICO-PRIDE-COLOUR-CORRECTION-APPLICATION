import numpy as np
from PIL import Image
from utils import Modify, LoadImage

def test_RGB_TO_LMS():
    expected_output = np.array([[17.8824, 43.5161, 4.11935],
                                [3.45565, 27.1554, 3.86714],
                                [0.0299566, 0.184309, 1.46709]])
    assert np.allclose(Modify.RGB_TO_LMS(), expected_output)

def test_LMS_TO_RGB():
    expected_output = np.array([[0.0809, -0.1305, 0.1167],
                                [-0.0102, 0.0540, -0.1136],
                                [-0.0004, -0.0041, 0.6935]])
    assert np.allclose(Modify.LMS_TO_RGB(), expected_output)

def test_colour_correction_matrix():
    expected_output = np.array([[0.5, 0.5, 0],
                                [0.2, 0.8, 0],
                                [0.025, 0.025, 0.95]])
    assert np.allclose(Modify.colour_correction_matrix(0.8, 0.5), expected_output)

def test_process_RGB():
    expected_output = np.array([[[0.47058824, 0.54509804, 0.76470588],
                                 [0.32941176, 0.43137255, 0.60392157]],
                                [[0.5254902, 0.6, 0.80392157],
                                 [0.42352941, 0.5254902, 0.74117647]]])
    assert np.allclose(LoadImage.process_RGB('test_image.png'), expected_output)

def test_process_LMS():
    expected_output = np.array([[[4.92445078, 18.01805816, 2.4824436],
                                 [2.8687417, 12.18118844, 2.11124897]],
                                [[5.52851072, 20.16846931, 2.78295095],
                                 [3.89825591, 15.1627907, 2.58109186]]])
    assert np.allclose(LoadImage.process_LMS('test_image.png'), expected_output)