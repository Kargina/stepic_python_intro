import os
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
    
    def get_photo_file_ext(self):
        extension = os.path.splitext(self.photo_file_name)
        return(extension[1])


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        # print(body_whl.split('x')[2])
        try:
            self.body_width = float(body_whl.split('x')[0])
            self.body_height = float(body_whl.split('x')[1])
            self.body_length = float(body_whl.split('x')[2])
        except:
            pass

    def get_body_volume(self):
        volume = self.body_width * self.body_height * self.body_length
        return volume

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    result = []
    

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # skip header
        for row in reader:
            if any(row): # at least one value in list present
                car_list.append(row)

    for row in car_list:
        if row[2]:
            row[2] = int(row[2])
        if row[5]:
            row[5] = float(row[5])
    # print(car_list)
    for row in car_list:
        if row[0] == 'car':
            car = Car(row[1], row[3], row[5], row[2])
            result.append(car)
        elif row[0] == 'truck':
            truck = Truck(row[1], row[3], row[5], row[4])
            result.append(truck)
        elif row[0] == 'spec_machine':
            spec_machine = SpecMachine(row[1], row[3], row[5], row[6])
            result.append(spec_machine)

 

    # print(car_list)
    # print(result)
    return result

# get_car_list("cars.csv")