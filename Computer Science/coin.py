#homework
#flip a coin
#self taught

import random
import itertools

print("You flip a coin ten time the results are below")

results = {
    'heads': 0,
    'tails': 0,
}
sides = list(results.keys())

for i in range(10):
    results[random.choice(sides)] += 1

print('Heads:', results['heads'])
print('Tails:', results['tails'])
