from .anouar import anouar

class Python(anouar):
    def __init__(self, age, min_age, max_age):
        super().__init__("test", age, min_age, max_age)

    def is_passed(self):
        if (self.age >= self.min_age):
           return "Passed"

        elif (self.age <= self.max_age):
            return"not Passed"


    def _print(self):
        print(f"age: {self.age}, Min_age: {self.min_age}, max_age: {self.max_age}")
