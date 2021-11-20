from DifficultyEstymatorService import DifficultyEstymatorService


if __name__ == "__main__":
    des = DifficultyEstymatorService()
    print(des.isStepsSet())
    print(des.isIngredientsSet())
    des.setSteps(5)
    des.setIngredients(5)
    print(des.isStepsSet())
    print(des.isIngredientsSet())

    des.run_estimation()
