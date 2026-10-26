import gymnasium as gym
from stable_baselines3 import PPO

# 1. Create the environment (notice we removed render_mode="human" so it trains blazingly fast in the background!)
env = gym.make("LunarLander-v3")

# 2. Initialize the PPO model with a standard small network (MlpPolicy)
model = PPO("MlpPolicy", env, verbose=1)

# 3. Train the AI (100,000 steps is a great start for a laptop; a full million takes about 20 minutes)
print("Training has started! Watch ep_rew_mean in the terminal...")
model.learn(total_timesteps=100000)

# 4. Save the trained brain so we can load it later
model.save("lunar_lander_ppo")
print("Training complete! Model saved as 'lunar_lander_ppo.zip'.")