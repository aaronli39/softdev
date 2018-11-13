import random

def main():
    day = "https://api.nasa.gov/planetary/apod?api_key=fDt3yjMvHQXteTtvW2I68LVqNNJFXy2raPmyg7AX&date="
    day += str(random.randint(1995, 2018))
    day += "-"
    day += str(random.randint(1,12))
    day += "-"
    day += str(random.randint(1, 31))

    return day

def definite():
    day = "https://api.nasa.gov/planetary/apod?api_key=fDt3yjMvHQXteTtvW2I68LVqNNJFXy2raPmyg7AX&date="
    day += str(random.randint(1996, 2017))
    day += "-"
    day += str(random.randint(1,12))
    day += "-"
    day += str(random.randint(1, 28))

    return day
