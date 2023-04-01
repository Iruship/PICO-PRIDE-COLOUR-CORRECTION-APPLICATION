import unittest
import utils
import run
import colorCorrection
import getImages

class TestFlaskRoutes(unittest.TestCase):

    def setup(self):
        self.utils =utils.test_client()
        self.utils.testing = True

    def setup(self):
        self.colorCorrection =colorCorrection.test_client()
        self.colorCorrection.testing = True    
           
    def test_RGB_TO_LMS_route(self):
        response = self.utils.get('/RGB_TO_LMS')
        self.assertEqual(response.status_code, 200)

    def test_LMS_TO_RGB_route(self):
        response = self.utils.get('/LMS_TO_RGB')
        self.assertEqual(response.status_code, 200) 
    
    def test_correctImage_route(self):
        response = self.colorCorrection.get('/correctImage')
        self.assertEqual(response.status_code, 500)    

if __name__ == '__main__':
    unittest.main()