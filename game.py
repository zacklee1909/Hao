import pygame
import random
import sys
import streamlit as st
from time import sleep
st.title("Game chơi thử ")
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vượt Chướng Ngại Vật")
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size
player_speed = 10
obstacle_width, obstacle_height = 80, 20
obstacle_speed = 7
obstacles = []
goal_area = pygame.Rect(0, 0, WIDTH, 60)
def create_obstacle():
    x_pos = random.randint(0, WIDTH - obstacle_width)
    y_pos = random.randint(goal_area.height, HEIGHT // 2)
    obstacle = pygame.Rect(x_pos, y_pos, obstacle_width, obstacle_height)
    obstacles.append(obstacle)
def check_collision(player_rect, obstacles):
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            return True
    return False
def reset_game():
    global player_x, player_y, obstacles, goal_area
    player_x = WIDTH // 2
    player_y = HEIGHT - player_size
    obstacles = []
    goal_area = pygame.Rect(0, 0, WIDTH, 60)
clock = pygame.time.Clock()
def game_loop():
    global player_x, player_y, obstacles, goal_area
    running = True
    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
            player_y += player_speed
        pygame.draw.rect(screen, GREEN, goal_area)
        if len(obstacles) < 5:
            create_obstacle()
        for obstacle in obstacles:
            obstacle.y += obstacle_speed
            pygame.draw.rect(screen, RED, obstacle)
            if obstacle.y > HEIGHT:
                obstacles.remove(obstacle)
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        pygame.draw.rect(screen, BLUE, player_rect)
        if check_collision(player_rect, obstacles):
            font = pygame.font.Font(None, 72)
            lose_text = font.render("You lost", True, RED,)
            screen.blit(lose_text, (WIDTH // 2 - lose_text.get_width() // 2, HEIGHT // 2 - lose_text.get_height() // 2))
            pygame.display.flip()
            sleep(2) 
            running = False  
            retry_screen(" Play again ?")
        if player_rect.colliderect(goal_area):
            font = pygame.font.Font(None, 72)
            win_text = font.render("You won", True, GREEN)
            screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - win_text.get_height() // 2))
            pygame.display.flip()
            sleep(2) 
            running = False 
            retry_screen("Không thắng nữa tao chịu")
        pygame.display.flip()
        clock.tick(30)
def retry_screen(message):
    font = pygame.font.Font(None, 48)
    retry_text = font.render(message, True, BLUE)
    retry_text_x = WIDTH // 2 - retry_text.get_width() // 2
    retry_text_y = HEIGHT // 2 - retry_text.get_height() // 2
    screen.blit(retry_text, (retry_text_x, retry_text_y))
    screen.blit(retry_text, (WIDTH // 2 - retry_text.get_width() // 2, HEIGHT // 2 - retry_text.get_height() // 2))
    retry_prompt = pygame.font.Font(None, 36).render("Press R for replay, Q for exit", True, BLUE)
    retry_prompt_x = WIDTH // 2 - retry_prompt.get_width() // 2 
    retry_prompt_y = retry_text_y + retry_text.get_height() + 30
    screen.blit(retry_prompt, (retry_prompt_x, retry_prompt_y))
    pygame.display.flip()
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()  
                    return  
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()  
def start_game():
    while True:
        reset_game()  
        game_loop()   
start_game()
