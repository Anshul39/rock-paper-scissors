# RPS.py

def player(prev_play, opponent_history=[]):

    if prev_play == "":
        opponent_history.clear()
        return "R"

    opponent_history.append(prev_play)

    if len(opponent_history) < 3:
        return "R"

    last_two = "".join(opponent_history[-2:])
    counts = {}

    for i in range(len(opponent_history) - 2):
        pattern = "".join(opponent_history[i:i+2])
        if pattern == last_two:
            next_move = opponent_history[i+2]
            counts[next_move] = counts.get(next_move, 0) + 1

    if counts:
        predicted = max(counts, key=counts.get)
    else:
        predicted = max(set(opponent_history), key=opponent_history.count)

    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[predicted]