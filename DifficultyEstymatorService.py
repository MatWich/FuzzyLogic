from fuzzylogic.classes import Domain, Rule
from fuzzylogic.functions import triangular, trapezoid


class DifficultyEstymatorService:
    def __init__(self):
        self.steps = 0
        self.ingredients = 0
        self.domains = {"ingredients": None, "steps": None, "difficulty": None}
        self.create()

    def create(self):
        """ Manager for all create methods"""
        self.create_domains()
        self.create_rules()

    def create_rules(self):
        """ This will create all rules that are needed """
        pass

    def create_domains(self):
        """ Creates all domains for in and out variables"""
        # IN
        self.domains["steps"] = Domain("Number of Steps", 1, 20)
        self.domains["ingredients"] = Domain("Number of Ingredients", 1, 20)
        # OUT
        self.domains["difficulty"] = Domain("Difficulty", 1, 5)
        print("Creating Domains is done.")

    def setting_up_domains(self):
        """ Setting up all the variables in Domains """
        # IN
        self.domains["steps"].low = triangular(1, 4)
        self.domains["steps"].medium = triangular(3, 7)
        self.domains["steps"].high = triangular(7, 20)

        self.domains["ingredients"].low = triangular(1, 4)
        self.domains["ingredients"].medium = triangular(3, 7)
        self.domains["ingredients"].high = triangular(5, 20)

        # OUT
        self.domains["difficulty"].low = triangular(1, 3)
        self.domains["difficulty"].medium = triangular(2, 4)
        self.domains["difficulty"].high = triangular(3, 5)
        print("Setting up Domains is done.")



    """ Getters and Setters """
    def getSteps(self):
        return self.steps

    def setSteps(self, steps):
        self.steps = steps

    def getIngredients(self):
        return self.ingredients

    def setIngredients(self, ingredients):
        self.ingredients = ingredients
