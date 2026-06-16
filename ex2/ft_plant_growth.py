class Plant:
    def __init__(
        self,
        name: str = "",
        height: float = 0.0,
        age: int = 0,
        age_a_day: int = 1,
        grow_per_day: float = .1,
    ):
        self.name = name
        self.height = float(height)
        self.age = int(age)
        self.age_a_day = int(age_a_day)
        self.grow_per_day = float(grow_per_day)

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}, {self.age} days old")

    def grow(self):
        self.height *= (1 + self.grow_per_day)
        return self.height

    def age_day(self):
        self.age += self.age_a_day
        return self.age

    def simulate_day(self):
        self.grow()
        self.age_day()


def main():
    plant1 = Plant("Rose", 50, 10)

    for days in range(1, 8):
        print(f"day{days}")
        plant1.simulate_day()

    plant1.show()


if __name__ == "__main__":
    main()
