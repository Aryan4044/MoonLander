# Lunar Lander Reinforcement Learning (PPO)

An autonomous reinforcement learning agent trained to land a lunar module safely between landing flags using **Gymnasium**, **Stable-Baselines3**, and **PyTorch**[cite: 1, 3]. 

This project implements **Proximal Policy Optimization (PPO)** to train a neural network policy from raw physics telemetry observations[cite: 1, 3].

---

## 🚀 Features

* **Reinforcement Learning Agent:** Utilizes a multi-layer perceptron policy (`MlpPolicy`) trained via PPO to optimize landing behaviors.
* **Physics Simulation:** Built on OpenAI/Farama Foundation's `Gymnasium` environment (`LunarLander-v3`) backed by Box2D physics[cite: 1, 3].
* **State Space Observation:** Processes 8 continuous state parameters per frame, including horizontal/vertical distance, velocity components, tilt angle, angular velocity, and ground-contact sensor data[cite: 1].
* **Action Space Control:** Manages 4 discrete actions (do nothing, fire left orientation engine, fire main descent engine, fire right orientation engine)[cite: 1, 2].
* **Interactive Manual Mode:** Includes a custom script to pilot the lander manually using keyboard inputs (`WASD`).

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Gymnasium** (Box2D physics environment)[cite: 3]
* **Stable-Baselines3** (RL algorithms & PPO implementation)[cite: 3]
* **PyTorch** (Deep learning backend)[cite: 3]
* **Pygame** (Rendering and keyboard event handling)

---