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

    def set_height(self, _height) -> None:
        if _height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else: 
            self._height = _height
            print(f"Height updated: {self._height}cm")

    def get_height(self) -> float:
        return self._height
    
    def set_age(self, _age) -> None:
        if _age < 0 :
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

    def simulate_day(self) ->None:
        self.grow()
        self.age_day()

    def simulate_days(self, days) -> float:
        initial = self.height
        for day in range(days):
            print(f"=== Day {day} ===")
            self.simulate_day()
            self.show()
        return self.height - initial
 
class Flower(Plant):
    def __init__(
            self, 
            name: str,
            height: float, 
            age: int, 
            color: str
            ):
        super().__init__(name, height, age)
        self.color = color

class Tree(Plant):
    def __init__(
            self, 
            name: str, 
            height: str, 
            age: int, 
            trunk_diameter: float
            ):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

class Vegetable(Plant):
    def __init__(
            self, 
            name: str, 
            height:float, 
            age:int, 
            harvest_season: str
            ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season