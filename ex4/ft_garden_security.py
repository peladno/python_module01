class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
    ):
        self.name = name
        self._height = height
        self._age = age

    def set_height(self, _height: float) -> None:
        if _height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = _height
            print(f"Height updated: {self._height}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, _age: int) -> None:
        if _age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = _age
            print(f"Age updated: {self._age} days")

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    def grow(self) -> float:
        self._height *= 1.1
        return self._height

    def age_day(self) -> int:
        self._age += 1
        return self._age

    def simulate_day(self) -> None:
        self.grow()
        self.age_day()

    def simulate_days(self, days: int) -> float:
        initial = self._height
        for day in range(days):
            print(f"=== Day {day} ===")
            self.simulate_day()
            self.show()
        return self._height - initial


def ft_garden_security():
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    print("Created: ", end="")
    plant.show()
    print("")
    plant.set_height(25.0)
    plant.set_age(30)
    print("")
    plant.set_height(-12)
    plant.set_age(-12)
    print("")
    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    ft_garden_security()
