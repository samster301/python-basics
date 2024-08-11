import random

NUM_OF_ATTEMPTS = 3
COUNTRY_POPULATION_MAP = {"US":330,"INDIA":1408,"CHINA":1420,"BRAZIL": 215}


def startGame():
    print("Hello Gamer")
    print(f"One of the countries from {COUNTRY_POPULATION_MAP.keys()}"
          f"would be randomly selected and you have {NUM_OF_ATTEMPTS} chances to guess its population."
          "I will let you know if your guess is Higher or Lower than the countries population")
    gameLogic()

def gameLogic():
    selectedCountry = random.choice(list(COUNTRY_POPULATION_MAP.keys()))
    selectedPopulation = COUNTRY_POPULATION_MAP.get(selectedCountry)
    print(selectedPopulation)

    for i in range(NUM_OF_ATTEMPTS):
        
        print(f" You have {NUM_OF_ATTEMPTS} attempts to guess")
        print (f"Attempt {i+1}")
        guessedPopulation = int(input("Enter the guess "))
        print(f"Your Guess is {guessedPopulation}")

        if  guessedPopulation < selectedPopulation:
            print("you need to go higher")
        elif guessedPopulation > selectedPopulation:
            print("you need to go lower")
        else:
            print("Bingo, you got it!")
            print(f"The Country is {selectedCountry}")
            break


startGame()