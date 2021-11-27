from DifficultyEstymatorService import DifficultyEstymatorService


if __name__ == "__main__":
    des = DifficultyEstymatorService()
    print(des.isStepsSet())
    print(des.isIngredientsSet())
    des.setSteps(12)
    des.setIngredients(9)
    print(des.isStepsSet())
    print(des.isIngredientsSet())

    des.run_estimation()
    # for share in des.getRulesShare():
    #     print(share)
