import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

def throw_two_dice():
    die = [1,2,3,4,5,6]
    die_1 = random.choices(die)
    die_2 = random.choices(die)
    dice = [die_1[0], die_2[0]]
    total = np.sum(dice)

    return total

n_times = 1000000
outcomes = []
for i in range(n_times):
    outcomes.append(throw_two_dice())

data = pd.DataFrame({'outcome': outcomes})
data = data.groupby(['outcome']).agg(n=('outcome', 'count')).reset_index()
data['probability'] = data['n'] / 1000000
data.plot(x='outcome', y='probability', kind='bar')