import pygame 
import random

# Game Variables
snake_speed = 25
window_x = 720
window_y = 720
black = pygame.Color(0,0 , 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

# Initialising pygameev
pygame.init()
pygame.display.set_caption('WHIZ SNAKE GAME')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

# Initialising snake position and size
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True
direction = 'DOWN'

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                direction = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                direction = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                direction = 'RIGHT'

    # Movement of the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        fruit_spawn = False
    else:
        snake_body.pop()

    # Fruit generation
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
    fruit_spawn = True

    # GFX
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game Over Loop
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    # Refresh game screen
    pygame.display.update()
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)