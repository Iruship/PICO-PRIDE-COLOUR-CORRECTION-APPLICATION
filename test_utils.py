import numpy as np
from PIL import Image
from utils import Modify, LoadImage


def test_RGB_TO_LMS():
    # test the RGB_TO_LMS function from Modify class
    expected = np.array([[0.02406428, 0.12662784, 0.01798225],
                         [0.0363012, 0.05586727, 0.02072684],
                         [0.00117722, 0.00246173, 0.06642638]])
    result = Modify.RGB_TO_LMS()
    assert np.allclose(result, expected)


def test_LMS_TO_RGB():
    # test the LMS_TO_RGB function from Modify class
    expected = np.array([[0.12195617, -0.01636173, -0.00412163],
                         [-0.04598248, 0.02960804, -0.00891848],
                         [0.01344424, -0.00276153, 0.09198326]])
    result = Modify.LMS_TO_RGB()
    assert np.allclose(result, expected)


def test_colour_correction_matrix():
    # test the colour_correction_matrix function from Modify class
    expected = np.array([[0.8, 0.2, 0],
                         [0.1, 0.9, 0],
                         [0.025, 0.025, 0.95]])
    result = Modify.colour_correction_matrix(0.2, 0.1)
    assert np.allclose(result, expected)


def test_process_RGB():
    # test the process_RGB function from LoadImage class
    expected = np.array([[[0.40784314, 0.50196078, 0.59215686],
                          [0.43529412, 0.52941176, 0.61960784]],
                         [[0.4, 0.49411765, 0.58431373],
                          [0.42745098, 0.52156863, 0.61176471]]])
    result = LoadImage.process_RGB('test_image.png')
    assert np.allclose(result, expected)


def test_process_LMS():
    # test the process_LMS function from LoadImage class
    expected = np.array([[[0.03468569, 0.06428112, 0.01128094],
                          [0.04515202, 0.07001444, 0.01232614]],
                         [[0.03316743, 0.06239445, 0.01098736],
                          [0.04363376, 0.06849617, 0.01179855]]])
    result = LoadImage.process_LMS('test_image.png')
    assert np.allclose(result, expected)
