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
player_score= 0
game_speed = 5
score_time1= 0
pygame.init()

font = pygame.font.Font("KA.ttf", 100)
font2 = pygame.font.Font("Minecraft.ttf", 30)
clock = pygame.time.Clock()
FPS = 40
        

def game_over():
    display_game_over = font.render ("GAME OVER!", True, yellow )
    screen.blit(display_game_over, (70, 170))

screen_width = 900
screen_height = 450
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("In the Wilderness")

frame_0 = pygame.image.load("assets/jumpcrop1.PNG")
frame_1 = pygame.image.load("assets/jumpcrop2.PNG")
frame_2 = pygame.image.load("assets/jumpcrop3.PNG")
frame_3 = pygame.image.load("assets/jumpcrop5.PNG")
frame_4 = pygame.image.load("assets/jumpcrop6.PNG")
frame_5 = pygame.image.load("assets/jumpcrop6.PNG")
frame_6 = pygame.image.load("assets/run1.PNG")
frame_7 = pygame.image.load("assets/run2.PNG")
frame_8 = pygame.image.load("assets/run3.PNG")
frame_9 = pygame.image.load("assets/run4.PNG")
frame_10 = pygame.image.load("assets/run5.PNG")
frame_11 = pygame.image.load("assets/run6.PNG")

fg = pygame.image.load("foreground_transparent.png").convert_alpha()

bg = pygame.image.load("nightforestbg.jpg").convert()
bg_width = bg.get_width()

tiles = math.ceil(screen_width / bg_width) + 1

floof = pygame.image.load("assets/idle1.png").convert_alpha()

obst1 = pygame.image.load("obstacles/bush1.png").convert_alpha()
obst2 = pygame.image.load("obstacles/bush2.png").convert_alpha()
obst3 = pygame.image.load("obstacles/bush3.png").convert_alpha()
obst4 = pygame.image.load("obstacles/bush4.png").convert_alpha()

advanced_width = int(obst1.get_width()* 0.32)
advanced_height = int(obst1.get_height()* 0.32)
obst1 = pygame.transform.scale(obst1, (advanced_width, advanced_height))
obst2 = pygame.transform.scale(obst2, (advanced_width, advanced_height))
obst3 = pygame.transform.scale(obst3, (advanced_width, advanced_height))
obst4 = pygame.transform.scale(obst4, (advanced_width, advanced_height))

new_width = int(floof.get_width() * 0.1)  
new_height = int(floof.get_height() * 0.1)  
floof = pygame.transform.scale(floof, (new_width, new_height))

new_w2 = int(frame_0.get_width()* 0.17)
new_h2 = int(frame_0.get_height()* 0.17)

#game speed
def main():
    global game_speed
    run = True
    clock = pygame.time.Clock()
    game_speed = 5

#score system
def score():
    global player_score, game_speed 
    player_score+=1
    if player_score % 100 == 0:
        game_speed +=1 
    
    text = font2.render("Points: " + str(player_score), True, yellow)
    textRect = text.get_rect()
    textRect.center = (800, 20)
    screen.blit(text, textRect)

#jump frames:
frame_0 = pygame.transform.scale(frame_0, (new_w2, new_h2))
frame_1 = pygame.transform.scale(frame_1, (new_w2, new_h2))
frame_2 = pygame.transform.scale(frame_2, (new_w2, new_h2))
frame_3 = pygame.transform.scale(frame_3, (new_w2, new_h2))
frame_4 = pygame.transform.scale(frame_4, (new_w2, new_h2))
frame_5 = pygame.transform.scale(frame_5, (new_w2, new_h2))

new_width2 = int(frame_6.get_width() * 0.17)
new_height2 = int(frame_6.get_height()*0.17)

#run frames:
frame_6 = pygame.transform.scale(frame_6, (new_width2, new_height2))
frame_7 = pygame.transform.scale(frame_7, (new_width2, new_height2))
frame_8 = pygame.transform.scale(frame_8, (new_width2, new_height2))
frame_9 = pygame.transform.scale(frame_9, (new_width2, new_height2))
frame_10 = pygame.transform.scale(frame_10, (new_width2, new_height2))
frame_11 = pygame.transform.scale(frame_11, (new_width2, new_height2))

jump_frames = [frame_0, frame_1, frame_2, frame_3, frame_4, frame_5]
walk_frames = [frame_6, frame_7, frame_8, frame_9, frame_10, frame_11]

def create_mask(image):
    return pygame.mask.from_surface(image)

bear_rect = pygame.Rect(200, player_y, frame_0.get_width(), frame_0.get_height()) 
bear_mask = create_mask(frame_0)  
frame_rate = 2
frame_index = 0
last_update = time.time()

floof_rect = jump_frames[0].get_rect()
floof_rect.x = 200
floof_rect.y = 70

frame_rate = 5
frame_index = 0
last_update = time.time()

obstacles = []

def generate_obstacle(last_x):
    x_position = last_x + 500 
    y_position = 255 
    obstacle_type = random.choice([obst1, obst2, obst3, obst4])  
    return [x_position, y_position, obstacle_type]

last_x = 0  
for i in range(3):  
    obstacles.append(generate_obstacle(last_x))
    last_x = obstacles[-1][0] 


running = True
is_jumping = False
jumping_peak_reached = False
while (running):

  clock.tick(FPS)

  for i in range(0, tiles):
   screen.blit(bg , (i * bg_width + scroll, 0))
 
   scroll -= 5
 
  if abs(scroll) > bg_width:
   scroll = 0

  screen.blit(fg, (0, 0))

  for obstacle in obstacles:
        x_pos, y_pos, obstacle_type = obstacle
        x_pos -= obstacle_speed
        if x_pos < -obstacle_type.get_width():
            x_pos = last_x + 500  
            last_x = x_pos  
        obstacle[0] = x_pos
        obstacle_rect = pygame.Rect(x_pos + 200, y_pos +200, obstacle_type.get_width(), obstacle_type.get_height())  # Bushes' Rect
        obstacle_mask = create_mask(obstacle_type)
        
        offset = (bear_rect.x - x_pos, bear_rect.y - y_pos)
        if bear_mask.overlap(obstacle_mask, offset):
            game_over() 
            pygame.display.update()
            pygame.time.delay(2000)  
            running = False  
 
        screen.blit(obstacle_type, (x_pos, y_pos))

  if is_jumping:
        
        current_frame = jump_frames[frame_index]
  else:
         
        current_frame = walk_frames[frame_index]

  bear = screen.blit(current_frame, (200, player_y))
  bear_rect.x = bear.x  
  bear_rect.y = bear.y  
  bear_mask = create_mask(current_frame)  

   
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                jumping_peak_reached = False  
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if player_y == 400:  
                    is_jumping = False

  if is_jumping:
      if frame_index < 5:
          current_time = time.time()
          if current_time - last_update >= 1 / frame_rate:
              frame_index += 1
              last_update = current_time
      else:
          frame_index = 5
  else:
      current_time = time.time()
      if current_time - last_update >= 1 / frame_rate:
          frame_index = (frame_index + 1)% len(walk_frames)
          last_update = current_time   

  if is_jumping:
        if not jumping_peak_reached:
            player_y -= 10  
            if player_y <= 70 - 130 : 
                jumping_peak_reached = True
        else: 
            player_y += 10 
            if player_y >= 225:  
                player_y = 225
                is_jumping = False  
                jumping_peak_reached = False
  score()


  #screen.blit(floof, (screen_width // 2 - floof.get_width() // 2, screen_height // 2 - floof.get_height() // 2))
  
  #screen.blit(frame_0, (170, 400))
  #screen.blit(frame_1, (180,145))
  #screen.blit(frame_2, (185, 125))
  #screen.blit(frame_3, (250, -20))
  #screen.blit(frame_4, (300, 10))
  #screen.blit(frame_5, (350, 30))
  
  pygame.display.update()              
pygame.quit()