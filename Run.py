from ColorCorrection import Main

def main():
    Main.correctImage(get_path='',
                      return_type='save',
                      save='Protanopia_corrected.png',
                      degree_of_protanopia=0.9,
                      degree_of_deutranopia=0.0)
    

    Main.correctImage(get_path='',
                      return_type='save',
                      save='Deutranopia_corrected.png',
                      degree_of_protanopia=0.0,
                      degree_of_deutranopia=1.0)
    

    Main.correctImage(get_path='',
                      return_type='save',
                      save='Hybrid_corrected.png',
                      degree_of_protanopia=0.5,
                      degree_of_deutranopia=0.5)
    
    return