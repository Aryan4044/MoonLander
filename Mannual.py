import gymnasium as gym
import pygame

# 1. Create the environment with a visible window
env = gym.make("LunarLander-v3", render_mode="human")
observation, info = env.reset()

running = True
print("--- MANUAL FLIGHT CONTROLS ---")
print("W = Main Engine")
print("A = Left Engine")
print("D = Right Engine")
print("Close the window to exit.")

while running:
    # Default action: do nothing
    action = 0 
    
    # Handle window close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read keyboard presses
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        action = 2  # Main engine
    elif keys[pygame.K_a]:
        action = 1  # Left engine
    elif keys[pygame.K_d]:
        action = 3  # Right engine

    # Step the game forward with your manual choice
    observation, reward, terminated, truncated, info = env.step(action)

    # If you crash or land, reset the game
    if terminated or truncated:
        observation, info = env.reset()

env.close()
pygame.quit()