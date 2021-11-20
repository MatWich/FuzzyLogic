from fuzzylogic.classes import Domain, Rule
from fuzzylogic.functions import triangular


class DifficultyEstymatorService:
    """ This class will calculate the difficulty of the recipe """

    def __init__(self):
        self.steps: int = 0
        self.ingredients: int = 0
        self.domains = {}
        self.rules = []
        self.result_rules = None
        self.create()

    def create(self):
        """ Manager for all create methods"""
        self.create_domains()
        self.setting_up_domains()
        self.create_rules()

    def create_rules(self):
        """ This will create all rules that are needed """
        self.rules.append(
            Rule({(self.domains["steps"].low, self.domains["ingredients"].low): self.domains["difficulty"].low}))
        self.rules.append(
            Rule({(self.domains["steps"].low, self.domains["ingredients"].medium): self.domains["difficulty"].low}))
        self.rules.append(
            Rule({(self.domains["steps"].low, self.domains["ingredients"].high): self.domains["difficulty"].medium}))

        self.rules.append(
            Rule({(self.domains["steps"].medium, self.domains["ingredients"].low): self.domains["difficulty"].medium}))
        self.rules.append(
            Rule({(self.domains["steps"].medium, self.domains["ingredients"].medium): self.domains[
                "difficulty"].medium}))
        self.rules.append(
            Rule({(self.domains["steps"].medium, self.domains["ingredients"].high): self.domains["difficulty"].high}))

        self.rules.append(
            Rule({(self.domains["steps"].high, self.domains["ingredients"].low): self.domains["difficulty"].medium}))
        self.rules.append(
            Rule({(self.domains["steps"].high, self.domains["ingredients"].medium): self.domains["difficulty"].high}))
        self.rules.append(
            Rule({(self.domains["steps"].high, self.domains["ingredients"].high): self.domains["difficulty"].high}))

        self.result_rules = Rule({
            (self.domains["steps"].low, self.domains["ingredients"].low): self.domains["difficulty"].low,
            (self.domains["steps"].low, self.domains["ingredients"].medium): self.domains["difficulty"].low,
            (self.domains["steps"].low, self.domains["ingredients"].high): self.domains["difficulty"].medium,

            (self.domains["steps"].medium, self.domains["ingredients"].low): self.domains["difficulty"].medium,
            (self.domains["steps"].medium, self.domains["ingredients"].medium): self.domains["difficulty"].medium,
            (self.domains["steps"].medium, self.domains["ingredients"].high): self.domains["difficulty"].high,

            (self.domains["steps"].high, self.domains["ingredients"].low): self.domains["difficulty"].medium,
            (self.domains["steps"].high, self.domains["ingredients"].medium): self.domains["difficulty"].high,
            (self.domains["steps"].high, self.domains["ingredients"].high): self.domains["difficulty"].high
        })

        print("Creating rules for model is done.")

    def create_domains(self):
        """ Creates all domains for in and out variables"""
        # IN
        self.domains["steps"] = Domain("Number of Steps", 1, 20, res=.1)
        self.domains["ingredients"] = Domain("Number of Ingredients", 1, 20, res=.1)
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
        self.domains["ingredients"].medium = triangular(3, 9)
        self.domains["ingredients"].high = triangular(8, 20)

        # OUT
        self.domains["difficulty"].low = triangular(1, 3)
        self.domains["difficulty"].medium = triangular(2, 4)
        self.domains["difficulty"].high = triangular(3, 5)
        print("Setting up Domains is done.")

    def run_estimation(self):
        """ Run the estimation """
        if self.isStepsSet() and self.isIngredientsSet():
            values = {self.domains["steps"]: self.steps, self.domains["ingredients"]: self.ingredients}
            print(self.result_rules(values))

    """ Helpers """

    def isStepsSet(self):
        return self.steps != 0

    def isIngredientsSet(self):
        return self.ingredients != 0

    """ Getters and Setters """

    def getSteps(self):
        return self.steps

    def setSteps(self, steps):
        self.steps = steps

    def getIngredients(self):
        return self.ingredients

    def setIngredients(self, ingredients):
        self.ingredients = ingredients
