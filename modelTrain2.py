import gymnasium as gym
from stable_baselines3 import PPO

# 1. Create the environment
env = gym.make("LunarLander-v3")

# 2. Load your existing model so it keeps all its past experience!
model = PPO.load("lunar_lander_ppo", env=env)

# 3. Train for more steps (let's add 400,000 more steps to push it further)
print("Resuming training to sharpen those parking skills...")
model.learn(total_timesteps=400000)

# 4. Save the upgraded model over your old file
model.save("lunar_lander_ppo")
print("Extended training complete! Upgraded model saved.")