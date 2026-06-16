class Plant:
  def __init__(self, name, heigth, age):
    self.name = name
    self.height = heigth
    self.age = age

  def print_info(self):
    print(f"{self.name}: {self.height}, {self.age} days old")

if __name__ == "__main__":
  plant1 = Plant("Rose", "25cm", 30)
  plant1.print_info()