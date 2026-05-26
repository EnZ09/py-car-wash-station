class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
    pass


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power,
                 average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        return round((car.comfort_class * (self.clean_power - car.clean_mark) *
                 self.average_rating / self.distance_from_city_center), 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, list_of_cars):
        income = 0
        for car in list_of_cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rate):
        sum_all_rate = self.average_rating * self.count_of_ratings
        sum_all_rate += rate
        self.count_of_ratings += 1
        self.average_rating = round(sum_all_rate / self.count_of_ratings, 1)
