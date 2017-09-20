class Human:
    name = ""
    male = False
    def __init__(self, name, gender):
        self.name = name
        self.male = gender

class BasicFeataures:
    bodyTypes = ["Ectomorph", "Endomorph", "Mesomorph"]
    age = 0
    bodyType = ""
    nationality = ""

    def __init__(self, age, bodyTypeNum, nationality):
        self.age = age
        self.bodyType = self.bodyType[bodyTypeNum]
        self.nationality = nationality



class FacialFeatures:
    hairStyles = ["Straight", "Curly", "Frizzy", "Wavy", "Coiled"]
    facialHairs = ["Moustache", "Mutton Chops", "Chin Strap", "Goatee", "Beard", "Gandalf",
                   "Fu Man Chu"]

    eyeColor = ""
    #SPECIFIC TO GIRLS
    hairStyle = ""
    #SPECIFIC TO GUYS
    facialHair = ""

    def __init__(self, gender, eyeColor, hairStyleNum, facialHairNum):
        self.eyeColor = eyeColor
        if gender:
            self.facialHair = self.facialHairs[facialHairNum]
        else:
            self.hairStyle = self.hairStyles[hairStyleNum]
    def __init__(self, eyeColor):

class Accessories:
    glasses = False
    jewelery = []

class bio:
    status = ["It's complicated", "Single", "In a relationship", "Married", "Divorved", "Asexual", "Bisexual"]
    interests = ""
    relationship = ""

def humanFeaturesInput():
    name = raw_input("Welcome! Please input your name to start: ")
    gendNum = 0
    while True:
        gender = input("Please input:\n"
                       "1) If you're a guy.\n"
                       "2) If you're a girl.")
        #if you're a guy
        if gender == 1:
            return Human(name, True)
        #ru guo ni shi nu hai
        elif gender == 2:
            return Human(name, False)
        else:
            print("Wrong input. Try again.")

def basicFeaturesInput():

    age = input("Please input your age: ")
    bodyTypeNum = 0

    while True:
        bodyTypeInput = input("Please input:\n"
                     "1) If you're an ectomorph.\n"
                     "2) If you're an endomorph.\n"
                     "3) If you're a mesomorph.")
        if bodyTypeInput is int and 1 <= bodyTypeInput <= 3:
            bodyTypeNum = bodyTypeInput
        else:
            print("Incorrect input. Please try again.")

    nationality = input("Please input your nationality.")
    return BasicFeataures(age, bodyTypeNum, nationality)


def facialFeaturesInput(gender):
    eyeColor = input("Please input your eye color: ")

    #if you're a guy
    if gender:
        var = input("Please input:\n"
                    "1) If you want facial hair."
                    "Anything else) If you don't want facial hair.")
        if var == 1:
            facialHairNum = input("Please input:\n"
                                  "1) Moustache\n"
                                  "2) Mutton Chops\n"
                                  "3) Chin Strap\n"
                                  "4) Goatee\n"
                                  "5) Beard\n"
                                  "6) Gandalf\n"
                                  "7) Fu Man Chu")
            return FacialFeatures(gender, eyeColor, None, facialHairNum)
        else:
            return facialFeatures(eyeColor)



    #ru guo ni shi nu hai
    if not gender:
        while True:
            hairStyleNum = input("Please input for your desired hair style:\n"
                    "1) Straight\n"
                    "2) Curly\n"
                    "3) Frizzy\n"
                    "4) Wavy \n"
                    "5) Coiled")
            if (1<=hairStyleNum<=5):
                return FacialFeatures(gender, eyeColor, hairStyleNum, None)
            else:
                print("Please try again.")



humanTraits = None
basicFeatures = None
facialFeatures = None
accessories = None
bio = None

while True:



