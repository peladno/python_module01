class Plant:
    class Statistics:
        def __init__(self):
            self._count_grow = 0
            self._count_age = 0
            self._count_show = 0

        def increase_grow(self) -> None:
            self._count_grow += 1

        def increase_age(self) -> None:
            self._count_age += 1

        def increase_show(self) -> None:
            self._count_show += 1

        def display(self) -> None:
            print(f"Stats: {self._count_grow} grow, "
                  f"{self._count_age} age, {self._count_show} show")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
    ):
        self.name = name
        self._height = height
        self._age = age
        self._statistics: Plant.Statistics = self.Statistics()

    def set_height(self, _height: float) -> None:
        self._height = _height
        if _height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
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
        self._statistics.increase_show()

    def grow(self) -> float:
        self._height += 1.2
        self._statistics.increase_grow()
        return self._height

    def age_day(self) -> int:
        self._age += 1
        self._statistics.increase_age()
        return self._age

    def simulate_day(self) -> None:
        self.grow()
        self.age_day()

    def simulate_days(self, days: int) -> float:
        initial = self._height
        print(f"[make tomato grow and age for {days} days]")
        for _ in range(days):
            self.simulate_day()
        return self._height - initial

    @staticmethod
    def check_age(days: int) -> None:
        if days > 365:
            print(f"Is {days} more than a year? -> True")
        else:
            print(f"Is {days} more than a year? -> False")

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def show_stats(self) -> None:
        self._statistics.display()


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            color: str,
    ):
        super().__init__(name, height, age)
        self.color = color
        self.is_bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color {self.color}")
        if self.is_bloomed == False:
            print(f" {self.name} is not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully")

    def to_bloom(self) -> None:
        self.is_bloomed = True

    def to_grow_bloom(self) -> None:
        self.grow()
        self.to_bloom()

    def to_grow_age_bloom(self) -> None:
        self.grow()
        self.to_bloom()
        self.age_day()


class Tree(Plant):
    class TreeStats(Plant.Statistics):
        def __init__(self):
            super().__init__()
            self._count_shade = 0

        def increase_shade(self) -> None:
            self._count_shade += 1

        def display(self) -> None:
            super().display()
            print(f" {self._count_shade} shade")

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            trunk_diameter: float
    ):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._statistics: Tree.TreeStats = self.TreeStats()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        self._statistics.increase_shade()
        print(
            f"Tree Oak now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            harvest_season: str,
            nutritional_value: int = 0
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def simulate_day(self) -> None:
        super().simulate_day()
        self.nutritional_value += 1


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self.count_seed = 0

    def to_bloom(self, seeds: int = 0) -> None:
        super().to_bloom()
        self.count_seed = seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.count_seed}")


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.show_stats()


def ft_garden_analytics() -> None:
    print("=== Garden statistics")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)
    print("")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "Red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.to_grow_bloom()
    rose.show()
    display_stats(rose)
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)
    print("")
    print("== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[asking the rose to grow and bloom]")
    sunflower.to_grow_age_bloom()
    sunflower.to_bloom(42)
    sunflower.show()
    display_stats(sunflower)
    print("")
    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_stats(unknown)


if __name__ == "__main__":
    ft_garden_analytics()
