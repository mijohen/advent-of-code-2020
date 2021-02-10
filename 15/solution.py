
def solution(end_turn):
    with open('input.txt') as file:
        line = file.readline().strip()
        values = line.split(',')

        turn = 0
        numbers = {}
        last_number = -1
        last_number_new = True

        # Say starting numbers
        for value in values:
            turn += 1
            numbers[int(value)] = turn
            last_number = int(value)

        while turn != end_turn:
            if last_number_new:
                numbers[last_number] = turn
                last_number = 0
            else:
                last_noticed = numbers[last_number]
                numbers[last_number] = turn
                last_number = int(turn) - int(last_noticed)

            last_number_new = last_number not in numbers
            turn += 1

        return last_number


print('part 1: ', solution(2020))
print('part 2: ', solution(30000000))
