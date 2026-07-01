#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, heigth: float, age: int):
        self.name = name
        self.height = heigth
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}, {self.age} days old")


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")

    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant(
            "Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    for plant in plants:
        plant.show()


if __name__ == "__main__":
    ft_garden_data()
