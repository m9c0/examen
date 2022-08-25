class Alive:
    def __init__(self, count):
        self.count = count

    def info(self):
        print("count:", self.count)

class Plants(Alive):
    def __init__(self, koef_repr, count):
        super().__init__(count)
        self.koef_repr = koef_repr

    def grown(self):
        self.count *= self.koef_repr

    def info(self):
        print("count plants:", self.count)

    def rebbits_food(self,count_rabbits):
        self.count -= count_rabbits * 10

    def add_plants(self,count_plants):
        self.count += count_plants



class Rabbits(Alive):
    def __init__(self, koef_repr, koef_death,count):
        super().__init__(count)
        self.koef_repr = koef_repr
        self.koef_death = koef_death

    def repriduction(self):
        self.count *= self.koef_repr

    def death(self):
        self.count -= int(self.count * self.koef_death)

    def info(self):
        print("count rabbits:", self.count)

    def take_away(self, count_rabbits):
        self.count -= count_rabbits


class Fox(Alive):
    def __init__(self, koef_repr, koef_death,count):
        super().__init__(count)
        self.koef_repr = koef_repr
        self.koef_death = koef_death

    def repriduction(self):
        self.count *= self.koef_repr

    def death(self):
        self.count -= int(self.count * self.koef_death)

    def info(self):
        print("count fox:", self.count)

    def take_away(self, count_fox):
        self.count -= count_fox


plants = Plants(10, 200)
rabbits = Rabbits(5, 0.2, 180)
foxs  = Fox(7, 0.3, 70)


year = 1
print("begin: ")
plants.info()
rabbits.info()
foxs.info()

while year <= 10:

    if plants.count // 10 <= rabbits.count:
        print("Warning!!!!!!!!!")
        print("platns is very low:")
        rabbits.info()
        plants.info()
        choise = int(input("enter 1 - add plants 2 - take away rabbits"))
        if choise == 1:
            count = int(input("enter count plants: "))
            plants.add_plants(count)
        elif choise == 2:
            count = int(input("enter count rabbits: "))
            rabbits.take_away(count)

    if plants.count <= 0 or rabbits.count <= 0:
        print("Fatality on year:", year)
        print("All our alive is death")
        break

    plants.grown()
    plants.rebbits_food(rabbits.count)

    rabbits.death()
    rabbits.repriduction()

    print("year: ", year)
    plants.info()
    rabbits.info()
    year += 1


