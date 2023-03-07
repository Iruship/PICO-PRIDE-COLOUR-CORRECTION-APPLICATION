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
                     save_path:str = None):
     
      #Loading the image file in LMS colour space. 
     rgb_image = LoadImage.process_RGB(get_path)

     modify = Modify.colour_correction_matrix(degree_of_deutranopia = degree_of_deutranopia,
                                              degree_of_protanopia = degree_of_protanopia) 
     
     corrected_image = np.uint8(np.dot(rgb_image,modify)*255)

     if return_type == 'save':
        assert save_path is not None , 'Save path is not provided for image!'
        cv2.imwrite(save_path,corrected_image)
        return
     
     if return_type == 'np':
        return corrected_image
     
     if return_type == 'pil':
        return Image.fromarray(corrected_image)

    
  
def parse_args():
   parser= argparse.ArgumentParser(
      description = 'Colour Correct Images for Colour-Blindness')

   parser.add_argument(
      '-input', type =str, help ='Path to input image.')
   parser.add_argument(
      '-output' , type = str, help = 'Path to save the output image dir.')
   parser.add_argument('-colours_correct', action = 'store_true', default=False, 
                       help = 'Corrected Image for Protonopia')
   parser.add_argument('-run_all',action = 'store_true', default=False,
                        help = 'Perform all corrections.' )
   parser.add_argument('-degree_of_protonopia', type = float, default =1.0, 
                       help = 'Adjust the degree of protonopia. Default is 1.0')
   parser.add_argument('-degree_of_deutranopia', type = float, default =1.0,
                        help = 'Adjust the degree of deutranopia Default is 1.0')
   
   args = parser.parse_args()

   return args   


def main():
    args = parse_args()

    get_path = args.input
    if get_path is None:
        print('Input image path not provided!')
        return

    get_path = args.input
    name_of_image = get_path.split('/')[-1]
    image_output_path = args.output

    assert os.path.isdir(image_output_path),'Output path should be a Directory'

    run_all = False
    if args.run_all:
        run_all = True

        if args.colours_correct or run_all:
            Main.correctImage(get_path= get_path,
                               return_type='save',
                               save_path = '{}/{}_{}'.format(image_output_path,'colours_correct', name_of_image),
                               degree_of_protanopia=args.degree_of_protonopia,
                               degree_of_deutranopia=args.degree_of_deutranopia)

    print('Completed running! Check output Image in {}'.format(image_output_path))

if __name__== '__main__':
   main()  



