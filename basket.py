import time
import random


class Team:
    def __init__(self, name, points, possessions, stats):
        self.name = name
        self.points = points
        self.possessions = possessions
        self.stats = stats

lakers = Team("Lakers", 0, 0, [0, 0, 0, 0, 0, 0, 0, 0])
celtics = Team("Celtics", 0, 0, [0, 0, 0, 0, 0, 0, 0, 0])


# main loop function
def play(x):
    x = duration_check(x)

    if x == 0:
        print("Lakers have the ball")
        lakers.possessions += 1
    elif x == 1:
        print("Celtics have the ball")
        celtics.possessions += 1

    chance = random.randint(1, 100)          # shot, foul or turnover
    three_chance = random.randint(1, 100)    # 2p or 3p shot
    two_made = random.randint(1, 100)        # 2p accuracy
    three_made = random.randint(1, 100)      # 3p accuracy
    bonus_chance = random.randint(1, 20)
    if chance < 81:                         # shot
        if three_chance < 40:               # 3p shot
            if three_made < 34:             # 3p shot made
                print("three points!")
                if x == 0:
                    lakers.points += 3
                    lakers.stats[2] += 1
                    lakers.stats[3] += 1
                    board()
                    if bonus_chance < 3:
                        x = bonus(x)
                    else:
                        x = ball_change(x)
                else:
                    celtics.points += 3
                    celtics.stats[2] += 1
                    celtics.stats[3] += 1
                    board()
                    if bonus_chance < 3:
                        x = bonus(x)
                    else:
                        x = ball_change(x)
            else:
                print("three points shot missed")
                if x == 0:
                    lakers.stats[2] += 1
                else:
                    celtics.stats[2] += 1
                x = rebound(x)
        else:                               # 2p shot
            if two_made < 51:               # 2p shot made
                print("two points")
                if x == 0:
                    lakers.points += 2
                    lakers.stats[0] += 1
                    lakers.stats[1] += 1
                    board()
                    if bonus_chance < 5:
                        x = bonus(x)
                    else:
                        x = ball_change(x)
                else:
                    celtics.points += 2
                    celtics.stats[0] += 1
                    celtics.stats[1] += 1
                    board()
                    if bonus_chance < 5:
                        x = bonus(x)
                    else:
                        x = ball_change(x)
            else:
                print("two points shot missed")
                if x == 0:
                    lakers.stats[0] += 1
                else:
                    celtics.stats[0] += 1
                x = rebound(x)
    elif 81 <= chance < 90:       # foul
        print("foul!")
        x = free_throw(x)
    else:
        if random.randint(0, 1) == 0:
            print("turnover")
        else:
            print("steal")
        x = ball_change(x)
    return x


# rebound action
def rebound(x):
    chance = random.randint(1, 100)
    if chance < 77:
        x = 1 - x
        print("defensive rebound")
        if x == 0:
            lakers.stats[6] += 1
        else:
            celtics.stats[6] += 1
    else:
        print("offensive rebound!")
        if x == 0:
            lakers.stats[7] += 1
        else:
            celtics.stats[7] += 1
    return x


# two free throws
def free_throw(x):
    total = 0
    while total < 2:
        chance = random.randint(1, 100)
        total += 1
        if chance < 76:
            print("free throw made")
            if x == 0:
                lakers.points += 1
                lakers.stats[4] += 1
                lakers.stats[5] += 1
            else:
                celtics.points += 1
                celtics.stats[4] += 1
                celtics.stats[5] += 1
            board()
            if total == 2:
                x = ball_change(x)
        else:
            print("free throw missed")
            if x == 0:
                lakers.stats[4] += 1
            else:
                celtics.stats[4] += 1
            if total == 2:
                x = rebound(x)
    return x


# bonus free throw
def bonus(x):
    print("and foul!")
    chance = random.randint(1, 100)
    if chance < 76:
        print("free throw made")
        if x == 0:
            lakers.points += 1
            lakers.stats[4] += 1
            lakers.stats[5] += 1
        else:
            celtics.points += 1
            celtics.stats[4] += 1
            celtics.stats[5] += 1
        board()
        x = ball_change(x)
    else:
        print("free throw missed")
        if x == 0:
            lakers.stats[4] += 1
        else:
            celtics.stats[4] += 1
        x = rebound(x)
    return x


# ball possession
def ball_change(x):
    x = 1 - x
    return x


# check the end of each period
def duration_check(x):
    if len(quarters) == 1:
        if lakers.possessions + celtics.possessions == pos_quarters[0]:
            print(" \nEnd of the first quarter\n ")
            quarters.append(1 - quarters[0])
            x = quarters[1]
    elif len(quarters) == 2:
        if lakers.possessions + celtics.possessions == (pos_quarters[0] + pos_quarters[1]):
            print(" \n---------\nHalftime!\n---------\n ")
            quarters.append(1 - quarters[1])
            x = quarters[2]
    elif len(quarters) == 3:
        if lakers.possessions + celtics.possessions == (pos_quarters[0] + pos_quarters[1] + pos_quarters[2]):
            print(" \nEnd of the third quarter\n ")
            quarters.append(1 - quarters[2])
            x = quarters[3]
    #elif len(quarters) == 4:
        #if lakers.possessions + celtics.possessions == (pos_quarters[0] + pos_quarters[1] + pos_quarters[2] + pos_quarters[3]):
            #end_game()
    return x


# the end of the game
def end_game():
    print("The game is over!")
    board()
    if lakers.points > celtics.points:
        print("Lakers wins!\n")
        final_stats()
    else:
        print("Celtics wins!\n")
        final_stats()


# the board
def board():
    print(lakers.name, lakers.points, celtics.points, celtics.name)


# incredible real stats (?)
def final_stats():
    print("Lakers stats\n------------")
    print("2 Points: ", lakers.stats[1], "-", lakers.stats[0])
    print("2 Points Perc.: ", round(lakers.stats[1]/lakers.stats[0]*100, 1), "%")
    print("3 Points: ", lakers.stats[3], "-", lakers.stats[2])
    print("3 Points Perc.: ", round(lakers.stats[3]/lakers.stats[2]*100, 1), "%")
    print("Free Throws: ", lakers.stats[5], "-", lakers.stats[4])
    print("Free Throws Perc.: ", round(lakers.stats[5]/lakers.stats[4] * 100, 1), "%")
    print("Defensive Rebounds:", lakers.stats[6])
    print("Offensive Rebounds:", lakers.stats[7])
    print("Total Rebounds:", lakers.stats[6]+lakers.stats[7])
    print()
    print("Celtics stats\n-------------")
    print("2 Points: ", celtics.stats[1], "-", celtics.stats[0])
    print("2 Points Perc.: ", round(celtics.stats[1]/celtics.stats[0] * 100, 1), "%")
    print("3 Points: ", celtics.stats[3], "-", celtics.stats[2])
    print("3 Points Perc.: ", round(celtics.stats[3]/celtics.stats[2] * 100, 1), "%")
    print("Free Throws: ", celtics.stats[5], "-", celtics.stats[4])
    print("Free Throws Perc.: ", round(celtics.stats[5]/celtics.stats[4] * 100, 1), "%")
    print("Defensive Rebounds:", celtics.stats[6])
    print("Offensive Rebounds:", celtics.stats[7])
    print("Total Rebounds:", celtics.stats[6] + celtics.stats[7])


# this determines the numbers of possessions per quarter
pos_quarters = [random.randint(47, 54), random.randint(47, 54), random.randint(47, 54), random.randint(47, 54), random.randint(14, 22)]
# global variables
ball = 0
lakers_end_possessions = 0
celtics_end_possessions = 0
quarters = []

# the game begins
board()
print("\nGAME ON!\n ")

# opening jump ball
if random.randint(0, 1) == 0:
    ball = 0
    quarters = [0]
    lakers.possessions += 1
    print("Lakers wins the opening jump ball")
else:
    ball = 1
    quarters = [1]
    celtics.possessions += 1
    print("Celtics wins the opening jump ball")

# action!
while lakers.possessions + celtics.possessions <= (pos_quarters[0] + pos_quarters[1] + pos_quarters[2] + pos_quarters[3]):
    ball = play(ball)

ball = random.randint(0, 1)
lakers_end_possessions = lakers.possessions
celtics_end_possessions = celtics.possessions
if lakers.points == celtics.points:
    print(" \n-----------\nOVERTIME!!!\n-----------\n ")
    time.sleep(3)
    while lakers.points == celtics.points:
        lakers.possessions = lakers_end_possessions
        celtics.possessions = celtics_end_possessions
        while lakers.possessions + celtics.possessions <= (pos_quarters[0] + pos_quarters[1] + pos_quarters[2] + pos_quarters[3] + pos_quarters[4]):
            ball = play(ball)
    end_game()
else:
    end_game()
