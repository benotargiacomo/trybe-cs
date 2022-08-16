def most_requested_by_name(name, orders):
    food_count = dict()

    for order in orders:
        if name in order:
            food = order.split(",")[1]
            if food not in food_count:
                food_count[food] = 1
            else:
                food_count[food] += 1

    return max(food_count, key=food_count.get)


def food_count(name, food, orders):
    food_count = 0

    for order in orders:
        if name in order and food in order:
            food_count += 1

    return food_count


def never_ask(client, orders):
    foods = {order.split(',')[1] for order in orders}

    ordered = {
        order.split(',')[1] for order in orders if client in order
    }

    return foods.difference(ordered)


def never_went(client, orders):
    days = {order.split(',')[2].replace('\n', '') for order in orders}

    frequency = {
        o.split(',')[2].replace('\n', '') for o in orders if client in o
    }

    return days.difference(frequency)


def analyze_log(path_to_file):
    if not ('.csv') in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, "r") as file:
            orders = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    with open('data/mkt_campaign.txt', 'w') as output_file:
        output_file.write(f"{most_requested_by_name('maria', orders)}\n")
        output_file.write(f"{food_count('arnaldo', 'hamburguer', orders)}\n")
        output_file.write(f"{never_ask('joao', orders)}\n")
        output_file.write(f"{never_went('joao', orders)}\n")
