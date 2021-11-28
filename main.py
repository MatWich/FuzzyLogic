from DifficultyEstymatorService import DifficultyEstymatorService


if __name__ == "__main__":
    steps = int(input("Podaj ilosc krokow w przepisie: "))
    ingredients = int(input("Podaj ilosc składników w przepisie: "))
    if steps <= 12 and ingredients <= 14:
        des = DifficultyEstymatorService()
        des.setSteps(steps)
        des.setIngredients(ingredients)

        des.run_estimation()
    else:
        raise Exception("values out of range")

