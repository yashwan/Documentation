from typing import List

class Actor:
    name:str = None
    age:str = None
    fav_movie = "Devara"
    __favorite_food: str = "Bavarchi Biryani"
    __personal_fav:List[str] = ["thelidu", "gurthuledu", "marchipoya"]
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def add_items_to_personal_fav(self, lis:List):
        self.__personal_fav += lis
    def display(self):
        print(self.name, self.age, self.__favorite_food, self.__personal_fav)



class Protagnist(Actor):
    def __init__(self, name, age, movie_name):
        super().__init__(name, age)
        self.movie_name = movie_name
        print(self.__favorite_food)
        print(self.fav_movie)

ntr = Actor("ntr", "36")
ntr.display()


prot = Protagnist("ntr", "36", "Adhurs")