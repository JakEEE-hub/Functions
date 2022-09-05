import random

country_cities = {"Czech Republic":"Prague", "Italy":"Rome", "Cyprus":"Nicosia", "Finland":"Helsinki",
                  "Denmark":"Copenhagen", "Germany":"Berlin", "Russia":"Moscow", "Kosovo":"Pristina",
                  "Bosnia":"Sarajevo", "San marino":"San marino", "Romania":"Bucharest", "Sweden":"Stockholm",
                  "Netherlands":"Amsterdam", "Luxembourg":"Luxembourg", "Latvia":"Riga", "Ireland":"Dublin",
                  "Montenegro":"Pod gorica", "Iceland":"Reykjavik", "Estonia":"Tallinn", "North macedonia":"Skopje",
                  "Norway":"Oslo", "Belarus":"Minsk", "Malta":"Valletta", "Austria":"Vienna", "Liechtenstein":"Vaduz",
                  "Spain":"Madrid", "Albania":"Tirana", "Serbia":"Belgrade", "Poland":"Warsaw", "Switzerland":"Bern",
                  "France":"Paris", "Andorra":"Andorra la vella", "Bulgaria":"Sofia", "Moldova":"Chisinau",
                  "Monaco":"Monaco", "Portugal":"Lisbon", "Ukraine":"Kyiv", "Slovenia":"Ljubljana", "Lithuania":"Vilnius",
                  "Greece":"Athens", "Belgium":"Brussels", "Hundary":"Budapest", "Croatia":"Zagreb", "Slovakia":"Slovakia",
                  "UK":"London"}

print("You're playing geography quiz!!\nWe'll give you 5 countries!!")

def play_game():
    true = 0
    for i in range(5):
        country = random.choice(list(country_cities.keys()))
        city_true = country_cities.get(country)
        answer = input(f"What is the capital city of {country} ?\n")
        if answer == city_true:
            true += 1
    print(f"You got {true} answers right!")

play_game()

while True:
    selection = input("Yay, try again?\nA) Ye sure\nB) A-a\n")

    if selection.upper() == "A":
        play_game()
    else:
        break




