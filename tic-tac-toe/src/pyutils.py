'''utility class for some needed functions'''
import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), "..")) #gives location of directory where script is stored

class Colors:
    RED = (168, 50, 50)
    BLUE = (50, 141, 168)
    BLACK = (0,0,0)
    TBLUE = (11, 109, 222)

if __name__ == "__main__":
    print("I am a utility function")