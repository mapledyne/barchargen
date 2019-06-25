import random
import bisect

genderlist = (
    ('male', 100),
    ('female', 100),
    ('gender fluid', 10),
)

racelist = (
    ('dragonborn', 50),
    ('dwarf', 100),
    ('elf', 100),
    ('gnome', 50),
    ('half-elf', 100),
    ('halfling', 100),
    ('half-orc', 50),
    ('human', 200),
    ('tiefling', 50),
)

# Returns a random value, considering the weights of each item.
class WeightedChoice(object):
    def __init__(self, weights):
        self.totals = []
        self.weights = weights
        running_total = 0

        for w in weights:
            running_total += w[1]
            self.totals.append(running_total)

    def next(self):
        rnd = random.random() * self.totals[-1]
        i = bisect.bisect_right(self.totals, rnd)
        return self.weights[i][0]

class Chargen(object):
    def __init__(self, seed):
        self.seed = seed
        random.seed(self.seed)
 
        self.gender = WeightedChoice(genderlist).next()
        self.race = WeightedChoice(racelist).next()
