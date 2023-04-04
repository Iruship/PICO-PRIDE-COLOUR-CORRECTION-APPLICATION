import unittest
import os

from PIL import Image
import numpy as np

from colorCorrection import Main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.image_path = "test_image.png"
        self.save_dir = "test_output"
        os.makedirs(self.save_dir, exist_ok=True)
        self.image = Image.new('RGB', (100, 100), color='red')
        self.image.save(self.image_path)
        self.protanopia = 0.5
        self.deutranopia = 0.5
    
    def tearDown(self):
        os.remove(self.image_path)
        os.rmdir(self.save_dir)

    def test_correctImage_return_type_np(self):
        corrected_image = Main.correctImage(self.image_path, self.protanopia, self.deutranopia, return_type_image='np')
        self.assertIsInstance(corrected_image, np.ndarray)
        self.assertEqual(corrected_image.shape, (100, 100, 3))

    def test_correctImage_return_type_pil(self):
        corrected_image = Main.correctImage(self.image_path, self.protanopia, self.deutranopia, return_type_image='pil')
        self.assertIsInstance(corrected_image, Image.Image)
        self.assertEqual(corrected_image.size, (100, 100))

    def test_correctImage_return_type_save(self):
        output_path = os.path.join(self.save_dir, "corrected_image.png")
        Main.correctImage(self.image_path, self.protanopia, self.deutranopia, return_type_image='save', save_path=output_path)
        self.assertTrue(os.path.exists(output_path))

if __name__ == '__main__':
    unittest.main()