import pygame
from random import random
import time
from pygame.locals import *
from logictictac import Game
from sys import exit
from pyutils import *

class App:
    ''''App loading class with needed functions'''

    def __init__(self) -> None:
        '''creates a new screen for the app and initialises the required modules'''

        self.screen = pygame.display.set_mode((640, 480))
        self.font1 = pygame.font.SysFont(None, 48)
        self.font2 = pygame.font.SysFont(None, 40)
        self.font3 = pygame.font.SysFont("ubuntumono", 55)
        self.font4 = pygame.font.SysFont("firamono", 60, True)
        float = random()
        if(float < 0.5):
            self.first_move = -1
        else:
            self.first_move = 1

    def load_media(self)-> None:
        '''loads the required images from the res folder'''

        #creating required filepaths
        grid_image_path = self.filepath("grid.png")
        logo_image_path = self.filepath("logo.png")
        bgmusic_path = self.filepath("bgmusic.mp3")
        zero_image_path = self.filepath("zero.png")
        cross_image_path = self.filepath("cross.png")
        
        #creating image surfaces
        self.logo_image = pygame.image.load(logo_image_path).convert_alpha()
        self.grid_image = pygame.image.load(grid_image_path).convert_alpha()
        self.zero_image = pygame.image.load(zero_image_path).convert_alpha()
        self.cross_image = pygame.image.load(cross_image_path).convert_alpha()
        self.grid_image = pygame.transform.scale(self.grid_image, (300, 300))
        self.zero_image = pygame.transform.scale(self.zero_image, (80, 80))
        self.cross_image = pygame.transform.scale(self.cross_image, (80, 80))

        #setting up caption and icon
        pygame.display.set_caption("TikiTikiTwoTwo")
        pygame.display.set_icon(self.logo_image)

        #setting up music 
        pygame.mixer.music.load(bgmusic_path)
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)
    
    def display_result(self, result: str, win_location: tuple) -> None:
        '''displays the result of the game conducted and reinitialises the move tracker'''

        if(result == "draw"):
            result = self.font4.render(f"NO ONE WINS", True, Colors.TBLUE)
            self.screen.blit(result, (100, 400))
        elif(result == "zero wins"):
            result = self.font4.render(f"PLAYER 1 WINS", True, Colors.TBLUE)
            self.screen.blit(result, (100, 400))
        elif(result == "cross wins"):
            result = self.font4.render(f"PLAYER 2 WINS", True, Colors.TBLUE)
            self.screen.blit(result, (100, 400))
        pygame.display.update()
        
        if(self.first_move == -1):
            self.first_move = 1
        else:
            self.first_move = -1
        time.sleep(1)

    def new_game_screen(self, score1: int, score2: int) -> None:
        '''creates a blank screen for a new game'''
        
        if(self.first_move == 1):
            display_text = self.font3.render("Player 1 moves first", True, Colors.BLACK)
        else:
            display_text =  self.font3.render("Player 2 moves first", True, Colors.RED)
        score_text = self.font1.render("SCORE", True, Colors.BLUE)
        player1_text = self.font2.render(f"Player 1: {score1}", True, Colors.BLACK)
        player2_text = self.font2.render(f"Player 2: {score2}", True, Colors.RED)
        self.screen.fill((255, 255, 255))
        self.screen.blit(display_text, (50,150))
        pygame.display.update()
        time.sleep(1.5)
        self.screen.fill((255,255,255))
        self.screen.blit(self.grid_image, (90, 80))
        self.screen.blit(score_text, (470, 100))
        self.screen.blit(player1_text, (430, 150))
        self.screen.blit(player2_text, (430, 200))
        pygame.display.update()

    @staticmethod
    def filepath(filename, root_folder="res"):
        ''''utility function to get file path for image in res'''
        return os.path.join(ROOT_DIR, root_folder, filename)

def convert_pos(pos: tuple) -> str:
    '''converts the mouse position into a grid description'''
    X = int(pos[0])
    Y = int(pos[1])
    if(X > 90 and X < 190):
        if(Y > 80 and Y < 180):
            return "topleft"
        elif(Y > 180 and Y < 280):
            return "middleleft"
        elif(Y > 280 and Y < 380):
            return "bottomleft"
        else:
            return "other"
    elif(X > 190 and X < 290):
        if(Y > 80 and Y < 180):
            return "topcentre"
        elif(Y > 180 and Y < 280):
            return "middlecentre"
        elif(Y > 280 and Y < 380):
            return "bottomcentre"
        else:
            return "other"
    elif(X > 290 and X < 390):
        if(Y > 80 and Y < 180):
            return "topright"
        elif(Y > 180 and Y < 280):
            return "middleright"
        elif(Y > 280 and Y < 380):
            return "bottomright"
        else:
            return "other"
    else:
        return "other"

def main() -> None:
    '''starts the main loop for the game'''

    #defining some dictionaries to help with logic and tracing of cursor
    coordinates = {
        "topleft": (0, 0), "topcentre": (0, 1), "topright": (0, 2),
        "middleleft": (1, 0), "middlecentre": (1, 1), "middleright": (1, 2),
        "bottomleft": (2, 0), "bottomcentre": (2, 1), "bottomright": (2, 2),
        "other": None
    }
    player_position = {
        "topleft": (100, 90), "topcentre": (200, 90), "topright": (300, 90),
        "middleleft": (100, 190), "middlecentre": (200, 190), "middleright": (300, 190),
        "bottomleft": (100, 290), "bottomcentre": (200, 290), "bottomright": (300, 290),
        "other": None
    }

    #tracking scores of the players
    score1 = 0
    score2 = 0

    #boolean variable for the main loop
    running = True 

    #initialising the class of the game
    app = App() 
    app.load_media()
    app.new_game_screen(score1, score2)
    game = Game()

    move = app.first_move
    move_no = 1

    while running: 
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
                pygame.quit()
                exit()
            elif(event.type == pygame.MOUSEBUTTONUP):
                mouse_pos = convert_pos(pygame.mouse.get_pos())
                if(mouse_pos == "other"):
                    continue
                else:
                    #if the grid is filled
                    if(move_no>9):
                        app.display_result("draw", (-1, -1))
                        move = app.first_move
                        app.new_game_screen(score1, score2)
                        move_no = 1
                        del game
                        game = Game()
                    else:
                        if(move == 1):
                            result, win = game.playmove("zero", coordinates.get(mouse_pos))

                            #checks if already a character is present at this position of the grid
                            if(result != "INVALID_POSITION"):
                                app.screen.blit(app.zero_image, player_position.get(mouse_pos))
                                pygame.display.update()
                                move -= 2
                                move_no += 1
                                if(result == "ZERO_WINS"):
                                    score1 += 1
                                    app.display_result("zero wins", win)
                                    app.new_game_screen(score1, score2)
                                    move = app.first_move
                                    move_no = 1
                                    del game
                                    game = Game()
                            pygame.display.update()
                        else:
                            result, win = game.playmove("cross", coordinates.get(mouse_pos))
                            if(result != "INVALID_POSITION"):
                                app.screen.blit(app.cross_image, player_position.get(mouse_pos))
                                pygame.display.update()
                                move += 2
                                move_no += 1
                                if(result == "CROSS_WINS"):
                                    score2 += 1
                                    app.display_result("cross wins", win)
                                    move = app.first_move
                                    app.new_game_screen(score1, score2)
                                    move_no = 1
                                    del game
                                    game = Game() 
                            pygame.display.update()
    pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    main()
