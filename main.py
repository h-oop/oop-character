#

class Character:
    # Constructor
    def __init__(self, name,phrase1,phrase2):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = 0
        print(f"Char created: {name}\n")


    # Methods
    def speak(self, phrase_num):
        if phrase_num == 1:
            print(self.phrase1)
        elif phrase_num == 2:
            print(self.phrase2)


    def set_lvl(self, lvl):
        self.level = lvl
        print(f"{self.name} is lvl {self.level}")



# set
char1 = Character("eeby", "i'm eeby", "i'm not deeby")
char2 = Character("bambam", "ayo i'm bambam", "in omnibus excelsior")
char3 = Character("Spiderman", "My Spider-Sense is tingling", "Your friendly neighbourhood spiderman.")


# act
char1.speak(1)
char2.set_lvl(2)
char3.speak(2)