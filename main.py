from DifficultyEstymatorService import DifficultyEstymatorService


if __name__ == "__main__":
    des = DifficultyEstymatorService()
    des.setSteps(12)
    des.setIngredients(9)

    des.run_estimation()

