import gym

#env = gym.make('CartPole-v0')
#env = gym.make('MountainCar-v0')
#env = gym.make('MsPacman-v0')
env = gym.make('Hopper-v1')
env.reset()

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())

env.close()