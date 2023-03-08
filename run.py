from colorCorrection import Main

def main():

    #Colour correcting image for Protanopia with diagnosed degree of 1.0 and saving the image.
    Main.correctImage(get_path='Correct_Image/original_image.jpg',
                      return_type_image='save',
                      save_path ='Correct_Image/Protanopia_corrected.png',
                      degree_of_protanopia=0.9,
                      degree_of_deutranopia=0.0)
    

    #Colour correcting image for Deutranopia with diagnosed degree of 1.0 and saving the image.
    Main.correctImage(get_path='Correct_Image/original_image.jpg',
                      return_type_image='save',
                      save_path='Correct_Image/Deutranopia_corrected.png',
                      degree_of_protanopia=0.0,
                      degree_of_deutranopia=1.0)
    
  #Colour correcting image for Hybrid with diagnosed degree of 1.0 for both Protanopia and Deutranopia and saving the image.
    Main.correctImage(get_path='Correct_Image/original_image.jpg',
                      return_type_image='save',
                      save_path='Correct_Image/Hybrid_corrected.png',
                      degree_of_protanopia=0.5,
                      degree_of_deutranopia=0.5)
    
    

    return

if __name__ == '__main__':
    main()
