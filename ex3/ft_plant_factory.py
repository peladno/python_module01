class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
    ):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}, {self.age} days old")

    def grow(self) -> float:
        self.height *= 1.1
        return self.height

    def age_day(self) -> int:
        self.age += 1
        return self.age

    def simulate_day(self) -> None:
        self.grow()
        self.age_day()

    def simulate_days(self, days) -> float:
        initial = self.height
        for day in range(days):
            print(f"=== Day {day} ===")
            self.simulate_day()
            self.show()
        return self.height - initial



def ft_plant_factory():
    plant_list = [
    Plant("Rose", 25, 13),
    Plant("Sunflower",10, 13),
    Plant("Oak", 5, 10),
    Plant("Fern",3, 2),
    Plant("Cactus", 1, 1.2),
    ]

    for plants in plant_list:
       print("Created: ", end="")
       plants.show()

if __name__ == "__main__":
    ft_plant_factory()
