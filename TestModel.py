import gymnasium as gym
from stable_baselines3 import PPO

# 1. Create the environment with a visible window so you can watch
env = gym.make("LunarLander-v3", render_mode="human")

# 2. Load your saved model from that .zip file
model = PPO.load("lunar_lander_ppo_old")

# 3. Let the trained AI take the wheel
observation, info = env.reset()

for _ in range(2000):
    # Ask the trained model what action to take (deterministic=True means it picks its best move)
    action, _states = model.predict(observation, deterministic=True)
    
    # Take the step in the game
    observation, reward, terminated, truncated, info = env.step(action)
    
    # If it lands or crashes, reset to watch it go again
    if terminated or truncated:
        observation, info = env.reset()

env.close()