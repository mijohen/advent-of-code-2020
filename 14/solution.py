from itertools import product


def decimal_to_binary(decimal, size):
    short_binary = bin(int(decimal))[2:]
    padding = size - len(short_binary)
    return '0'*padding + short_binary


def bitmask_value(binary_value, bitmask):
    new_value = ''

    for index, value in enumerate(bitmask):
        new_value += binary_value[index] if value == 'X' else value

    return new_value


def bitmask_memory_address(memory_address, bitmask):
    new_value = ''
    locations = []

    for index, value in enumerate(bitmask):
        if value == '0':
            new_value += memory_address[index]
        if value == '1':
            new_value += '1'
        if value == 'X':
            new_value += 'X'
            locations.append(index)

    results = []

    for combination in product([0, 1], repeat=len(locations)):
        result = list(new_value)

        for index, number in enumerate(combination):
            position = locations[index]
            result[position] = str(number)
        results.append("".join(result))

    return results


MASK_ID = 'mask ='
MEM_ID = 'mem['
SIZE = 36


def part_one():
    with open('input.txt') as file:
        bitmask = SIZE*'X'
        memory = {}

        for line in file:
            line = line.strip()

            if line.startswith(MASK_ID):
                bitmask = line.lstrip(MASK_ID)

            if line.startswith(MEM_ID):
                _, right_side = line.split(MEM_ID, 1)
                location, value = right_side.split('] = ')

                binary_value = decimal_to_binary(value, SIZE)
                masked_value = bitmask_value(binary_value, bitmask)
                decimal_value = int(masked_value, 2)
                memory[location] = decimal_value

        return sum(memory.values())


def part_two():
    with open('input.txt') as file:
        bitmask = SIZE*'0'
        memory = {}

        for line in file:
            line = line.strip()

            if line.startswith(MASK_ID):
                bitmask = line.lstrip(MASK_ID)

            if line.startswith(MEM_ID):
                _, right_side = line.split(MEM_ID, 1)
                location, value = right_side.split('] = ')

                binary_value = decimal_to_binary(location, SIZE)
                possible_locations = bitmask_memory_address(binary_value, bitmask)

                for possible_location in possible_locations:
                    location = int(possible_location, 2)
                    memory[location] = int(value)

        return sum(memory.values())


print('part 1: ', part_one())

print('part 2: ', part_two())

