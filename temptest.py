class Bus:
    def __init__(self, people = []) -> None:
        self.people = people

    def pick(self, person:str):
        self.people.append(person)

    def drop(self, person:str):
        self.people.remove(person)


b1 = Bus()
b2 = Bus()
b1.pick('a')
b1.pick('b')
print("Bus2: ", b2.people)