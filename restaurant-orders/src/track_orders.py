class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append({'customer': customer, 'order': order, 'day': day})

    def get_most_ordered_dish_per_customer(self, customer):
        food_count = dict()

        for order in self.orders:
            if customer in order['customer']:
                if order['order'] not in food_count:
                    food_count[order['order']] = 1
                else:
                    food_count[order['order']] += 1

        return max(food_count, key=food_count.get)

    def get_never_ordered_per_customer(self, customer):
        foods = {order['order'] for order in self.orders}

        ordered = {
            o['order'] for o in self.orders if customer in o['customer']
        }

        return foods.difference(ordered)

    def get_days_never_visited_per_customer(self, customer):
        days = {order['day'] for order in self.orders}

        frequency = {
            o['day'] for o in self.orders if customer in o['customer']
        }

        return days.difference(frequency)

    def get_busiest_day(self):
        days = dict()

        for order in self.orders:
            if order['day'] not in days:
                days[order['day']] = 1
            else:
                days[order['day']] += 1

        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = dict()

        for order in self.orders:
            if order['day'] not in days:
                days[order['day']] = 1
            else:
                days[order['day']] += 1

        return min(days, key=days.get)
