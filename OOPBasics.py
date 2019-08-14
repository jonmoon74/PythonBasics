class Fruit(object):
    def __init__(self, kind):
        print(kind)

    def nutrition(self):
        print("I am good for you")

    def color(self):
        print("I am turquoise")


class Peach(Fruit):
    def __init__(self, kind):
        print(kind)

    def shape(self):
        print("round")


f1 = Peach("Nectarine")
f2 = Fruit("Plum")

print(f1.shape())
#print(f2.shape())
print(f1.nutrition())
print(f2.nutrition())
