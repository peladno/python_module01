class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
    ):
        self.name = name
        self.height = float(height)
        self.age = int(age)

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}, {self.age} days old")

    def grow(self):
        self.height *= 1.1
        return self.height

    def age_day(self):
        self.age += 1
        return self.age

    def simulate_day(self):
        self.grow()
        self.age_day()

    def simulate_days(self, days):
        initial = self.height
        for day in range(days):
            print(f"=== Day {day} ===")
            self.simulate_day()
            self.show()
        return self.height - initial



def main():
    plant1 = Plant("Rose", 50, 10)
    print("=== Garden Plant Growth ===")
    diff = plant1.simulate_days(7)
    print(f"Growth this week: {diff:.1f}cm")


if __name__ == "__main__":
    main()
