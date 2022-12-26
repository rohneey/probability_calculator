import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = list()               # list of strings containing one item for each ball in the hat
        for color in kwargs:
            for _ in range(kwargs[color]):
                self.contents.append(color)

    def draw(self, balls_drawn):
        removed_balls = list()               
        if balls_drawn < len(self.contents):
            for _ in range(balls_drawn):
                removed_balls.append(self.contents.pop(random.randrange(len(self.contents))))    
            return removed_balls             # randomly drawned balls    
        else:
            return self.contents             # original set of balls if the number of balls to draw exceeds the available quantity

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = dict()
        lucky_draws = 0

        balls = hat_copy.draw(num_balls_drawn) # balls drawn during 1 experiment

        for color in balls:
            drawn_balls[color] = drawn_balls.get(color, 0) + 1 # dict containing balls colors and numbers

        for color in expected_balls.keys():
            if color in drawn_balls.keys():
                if  drawn_balls[color] >= expected_balls[color]:
                    lucky_draws += 1
                else:
                    0

                if lucky_draws == len(expected_balls):    # comparing exact amount of balls to expected
                    m += 1
                else:
                    0
        
    return m / num_experiments