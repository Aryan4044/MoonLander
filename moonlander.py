import gymnasium as gym

# 1. Create the Lunar Lander environment with a visible window
env = gym.make("LunarLander-v3", render_mode="human")

# 2. Reset the environment to start a new attempt
observation, info = env.reset()

# 3. Run a loop for 200 frames to watch it fail
for _ in range(200):
    # Pick a random action: 0 = do nothing, 1 = left engine, 2 = main engine, 3 = right engine
    action = env.action_space.sample() 
    
    # Take a step in the game using that action
    observation, reward, terminated, truncated, info = env.step(action)
    
    # Print the 8 numbers the AI receives (distance, speed, tilt, legs, etc.)[cite: 2]
    print("Observation numbers:", observation)

    # If the rocket crashes or lands, restart the attempt
    if terminated or truncated:
        observation, info = env.reset()

env.close()