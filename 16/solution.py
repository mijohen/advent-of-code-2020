EMPTY_LINE = '\n'


def solution():
    fields = {}
    field_names = []

    with open('input.txt') as file:

        for line in file:
            if line == EMPTY_LINE:
                break

            field, rules = line.strip().split(": ")
            first_rule, second_rule = rules.split(" or ")

            first_start, first_end = first_rule.split("-")
            second_start, second_end = second_rule.split("-")

            fields[field] = (
                range(int(first_start), int(first_end) + 1),
                range(int(second_start), int(second_end) + 1)
            )
            field_names.append(field)

        ignore_lines_in(file, lines=1)
        main_ticket = [int(ticket) for ticket in file.readline().strip().split(',')]
        ignore_lines_in(file, lines=2)

        tickets = file.readlines()
        total_of_invalid_ticket_numbers = 0
        ticket_field_index = {}
        valid_tickets = 0

        for ticket in tickets:
            ticket_numbers = [int(ticket) for ticket in ticket.strip().split(',')]
            invalid_ticket_numbers = get_invalid_ticket_numbers(ticket_numbers, fields)
            total_of_invalid_ticket_numbers += sum(invalid_ticket_numbers)

            # Ignore invalid tickets
            if invalid_ticket_numbers:
                continue

            valid_tickets += 1
            field_count_map = get_field_count(ticket_numbers, fields)

            # Merge field count
            for index, field_count in field_count_map.items():
                ticket_field_index.setdefault(index, {})
                global_field_map = ticket_field_index.get(index)
                for field_name, count in field_count.items():
                    global_field_map.setdefault(field_name, 0)
                    global_field_map[field_name] = global_field_map.get(field_name) + count

        final_names = []

        for index, ticket_number in enumerate(main_ticket):
            possible_fields = ticket_field_index.get(index)
            for field_name in field_names:
                count = possible_fields.get(field_name)
                if count == valid_tickets and field_name not in final_names:
                    final_names.append(field_name)
                    break

        multiple_result = 1
        for index, field_name in enumerate(final_names):
            if field_name.startswith("departure"):
                multiple_result *= main_ticket[index]

        print('Part 1: ', total_of_invalid_ticket_numbers)
        # TODO: Incorrect - Answer is too high
        print('Part 2: ', multiple_result)


def get_invalid_ticket_numbers(ticket_numbers, fields):
    invalid_ticket_numbers = []

    for index, ticket_number in enumerate(ticket_numbers):
        valid_ticket_number = False
        for first_range, second_range in fields.values():
            if ticket_number in first_range or \
                    ticket_number in second_range:
                valid_ticket_number = True
                break

        if not valid_ticket_number:
            invalid_ticket_numbers.append(ticket_number)

    return invalid_ticket_numbers


def get_field_count(ticket_numbers, fields):
    ticket_field_index = {}

    for index, ticket_number in enumerate(ticket_numbers):
        ticket_field_index.setdefault(index, {})
        fields_for_index = ticket_field_index.get(index)

        for field_name, ranges in fields.items():
            first_range, second_range = ranges

            if ticket_number in first_range or ticket_number in second_range:
                fields_for_index.setdefault(field_name, 0)
                fields_for_index[field_name] = fields_for_index.get(field_name) + 1

    return ticket_field_index


def ignore_lines_in(file, lines=1):
    for i in range(lines):
        file.readline()


solution()
