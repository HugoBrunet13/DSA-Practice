

def get_final_position(moves):


    count_up = count_down = count_left = count_right = 0

    for move in moves:
        if move == "U":
            count_up += 1
        elif move == "D":
            count_down += 1
        elif move == "L":
            count_left += 1
        elif move == "R":
            count_right += 1

    return (count_right - count_left, count_up - count_down)



moves = "UDDLLRUUUDUURUDDUULLDRRRR"
print(get_final_position(moves))