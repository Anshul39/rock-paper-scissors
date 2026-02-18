import random

def play(player1, player2, num_games):
    p1_prev = ""
    p2_prev = ""
    p1_score = 0

    for _ in range(num_games):
        p1 = player1(p2_prev)
        p2 = player2(p1_prev)

        p1_prev = p1
        p2_prev = p2

        if (p1 == "R" and p2 == "S") or \
           (p1 == "P" and p2 == "R") or \
           (p1 == "S" and p2 == "P"):
            p1_score += 1

    win_rate = p1_score / num_games
    print("Win rate:", win_rate)
    return win_rate


# -------- BOTS --------

def quincy(prev_play):
    return "R"

def abbey(prev_play):
    return {"R": "P", "P": "S", "S": "R"}.get(prev_play, "R")

def kris(prev_play):
    return random.choice(["R", "P", "S"])

def mrugesh(prev_play):
    return random.choice(["R", "P", "S"])