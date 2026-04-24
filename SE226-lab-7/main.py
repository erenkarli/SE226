class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = int(year)

    def __str__(self):
        return f"VID: {self.vid} | {self.model} ({self.year})"

    def __eq__(self, other):
        return self.vid == other.vid

    def is_new(self, n):
        return (2026 - self.year) <= n


class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = int(doors)

    def __str__(self):
        return f"[Car] {super().__str__()} | Fuel: {self.fuel_type} | {self.doors} Doors"


class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = int(max_load)
        self.axles = int(axles)

    def __str__(self):
        return f"[Truck] {super().__str__()} | Load: {self.max_load}kg | {self.axles} Axles"


class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, type):
        super().__init__(vid, model, year)
        self.engine_cc = int(engine_cc)
        self.type = type

    def __str__(self):
        return f"[Motorcycle] {super().__str__()} | Eng: {self.engine_cc}cc | Type: {self.type}"


def save_fleet_to_file(vehicles, filename):
    with open(filename, 'w') as f:
        for v in vehicles:
            if isinstance(v, Car):
                f.write(f"Car, {v.vid}, {v.model}, {v.year}, {v.fuel_type}, {v.doors}\n")
            elif isinstance(v, Truck):
                f.write(f"Truck, {v.vid}, {v.model}, {v.year}, {v.max_load}, {v.axles}\n")
            elif isinstance(v, Motorcycle):
                f.write(f"Motorcycle, {v.vid}, {v.model}, {v.year}, {v.engine_cc}, {v.type}\n")


def load_fleet_from_file(filename):
    fleet = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                data = [item.strip() for item in line.split(',')]
                if not data or data[0] == "":
                    continue

                v_type = data[0]
                if v_type == "Car":
                    fleet.append(Car(data[1], data[2], data[3], data[4], data[5]))
                elif v_type == "Truck":
                    fleet.append(Truck(data[1], data[2], data[3], data[4], data[5]))
                elif v_type == "Motorcycle":
                    fleet.append(Motorcycle(data[1], data[2], data[3], data[4], data[5]))
        return fleet
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    initial_vehicles = [
        Car("V001", "Tesla Model 3", 2023, "Electric", 4),
        Truck("T101", "Volvo FH16", 2019, 25000, 6),
        Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport"),
        Car("V002", "Toyota Corolla", 2018, "Petrol", 4),
        Truck("T102", "Mercedes Actros", 2021, 18000, 4),
        Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
    ]

    save_fleet_to_file(initial_vehicles, "fleet.txt")

    print(f"Loading fleet data from 'fleet.txt'...")
    loaded_fleet = load_fleet_from_file("fleet.txt")
    print(f" {len(loaded_fleet)} vehicles loaded successfully.")

    print("\n --- All Vehicles ---")
    for v in loaded_fleet:
        print(v)

    print("\n --- Recent Vehicles (Last 4 Years) ---")
    for v in loaded_fleet:
        if v.is_new(5):
            print(v)

    print("\n --- Electric Cars Only ---")
    for v in loaded_fleet:
        if isinstance(v, Car) and v.fuel_type == "Electric":
            print(v)