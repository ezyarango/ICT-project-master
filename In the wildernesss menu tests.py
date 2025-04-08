import pygame 
import math
import random
import time
import sys

#variables library:
score = 0
scroll = 0
y_change = 0
gravity = 1
obstacles = (300, 450, 600, 750)
obstacle_speed = 5
active = True
player_x = 200
player_y = 225
active_frame = 0
mode = 0
count = 0
yellow = 252, 252, 179

pygame.init()

def main_menu(): #Main Menu screen
    screen_width = 900
    screen_height = 450
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("In the Wilderness: Menu")
    
    while True:
        screen_width = 900
        screen_height = 450
        BG = pygame.image.load("nightforestbg.jpg").convert()
        bg_width = BG.get_width()
        tiles = math.ceil(screen_width / bg_width) + 1
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        font = pygame.font.Font("KA.ttf", 100)


        MENU_TEXT = font.render("IN THE WILDERNESS", True, yellow)
        MENU_RECT = MENU_TEXT.get_rect(center=(550, 100))

        class Button():
            def _init_(self,image,pos,text_input,font,base_color,hovering_color):
                self.image = image
                self.x_pos = pos[0]
                self.y_pos = pos [1]
                self.font = font
                self.base_color, self.hovering_color= base_color, hovering_color
                self.text_unput = text_input
                self.text = self.font.render(self.text_input, True, self.base_color)
            if self.image is None:
                self.image = self.text.get_rect(center-(self.x_pos, self.y_pos))
            
            def update(self,screen):
                if self.image is not None:
                    screen.blit(self.image, self.rect)
                screen.blit(self.text, self.text_rect)
            
            def checkForInput(self, position):
                if position[o] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                    return True
                return False
            
            def changeColor(self, position):
                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                    self.text= self.text.font.render(self.text_input, True, self.hovering_color)
                else:
                    self.text= self.font.render(self.text_input, True, self.base_color)

        button = Button("KA.ttf", 550, 200, "PLAY")

        while True:
	        for event in pygame.event.get():
		        if event.type == pygame.QUIT:
			        pygame.quit()
			        sys.exit()
		        if event.type == pygame.MOUSEBUTTONDOWN:
			        button.checkForInput(pygame.mouse.get_pos())
            
            screen.fill("white")

	        button.update()
	        button.changeColor(pygame.mouse.get_pos())

	        pygame.display.update()

        PLAY_BUTTON = text_input= "PLAY", font= font(100),base_color=yellow,hovering_color= white, pos=(550,200)
        QUIT_BUTTON = text_input= "QUIT", font= font(75), base_color= yellow,hovering_color= white ,pos=(550,300)

        

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        


        

    