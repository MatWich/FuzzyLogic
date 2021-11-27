from fuzzylogic.classes import Domain, Rule
from fuzzylogic.functions import triangular, trapezoid


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
            Rule({(self.domains["steps"].low, self.domains["ingredients"].low): self.domains["difficulty"].v_easy}))
        self.rules.append(
            Rule({(self.domains["steps"].low, self.domains["ingredients"].medium): self.domains["difficulty"].v_easy}))
        self.rules.append(
            Rule({(self.domains["steps"].low, self.domains["ingredients"].high): self.domains["difficulty"].easy}))

        self.rules.append(
            Rule({(self.domains["steps"].medium, self.domains["ingredients"].low): self.domains["difficulty"].easy}))
        self.rules.append(
            Rule({(self.domains["steps"].medium, self.domains["ingredients"].medium): self.domains[
                "difficulty"].medium}))
        self.rules.append(
            Rule({(self.domains["steps"].medium, self.domains["ingredients"].high): self.domains["difficulty"].hard}))

        self.rules.append(
            Rule({(self.domains["steps"].high, self.domains["ingredients"].low): self.domains["difficulty"].medium}))
        self.rules.append(
            Rule({(self.domains["steps"].high, self.domains["ingredients"].medium): self.domains["difficulty"].v_hard}))
        self.rules.append(
            Rule({(self.domains["steps"].high, self.domains["ingredients"].high): self.domains["difficulty"].v_hard}))

        self.result_rules = Rule({
            (self.domains["steps"].low, self.domains["ingredients"].low): self.domains["difficulty"].v_easy,
            (self.domains["steps"].low, self.domains["ingredients"].medium): self.domains["difficulty"].v_easy,
            (self.domains["steps"].low, self.domains["ingredients"].high): self.domains["difficulty"].easy,

            (self.domains["steps"].medium, self.domains["ingredients"].low): self.domains["difficulty"].easy,
            (self.domains["steps"].medium, self.domains["ingredients"].medium): self.domains["difficulty"].medium,
            (self.domains["steps"].medium, self.domains["ingredients"].high): self.domains["difficulty"].hard,

            (self.domains["steps"].high, self.domains["ingredients"].low): self.domains["difficulty"].medium,
            (self.domains["steps"].high, self.domains["ingredients"].medium): self.domains["difficulty"].v_hard,
            (self.domains["steps"].high, self.domains["ingredients"].high): self.domains["difficulty"].v_hard
        })

        print("Creating rules for model is done.")

    def create_domains(self):
        """ Creates all domains for in and out variables"""
        # IN
        self.domains["steps"] = Domain("Number of Steps", 1, 12, res=.1)
        self.domains["ingredients"] = Domain("Number of Ingredients", 1, 14, res=.1)
        # OUT
        self.domains["difficulty"] = Domain("Difficulty", 1, 6)
        print("Creating Domains is done.")

    def setting_up_domains(self):
        """ Setting up all the variables in Domains """
        # IN
        self.domains["steps"].low = trapezoid(1, 2, 3, 5)
        self.domains["steps"].medium = triangular(4, 10)
        self.domains["steps"].high = trapezoid(8, 10, 12, 12.01)

        self.domains["ingredients"].low = trapezoid(1, 1.01, 4, 5)
        self.domains["ingredients"].medium = trapezoid(5, 7, 10, 12)
        self.domains["ingredients"].high = trapezoid(10, 12, 14, 14.01)

        # OUT
        self.domains["difficulty"].v_easy = triangular(0, 2)
        self.domains["difficulty"].easy = triangular(1, 3)
        self.domains["difficulty"].medium = triangular(2, 4)
        self.domains["difficulty"].hard = triangular(3, 5)
        self.domains["difficulty"].v_hard = triangular(4, 6)

        print("Setting up Domains is done.")

    def run_estimation(self):
        """ Run the estimation """
        if self.isStepsSet() and self.isIngredientsSet():
            values = {self.domains["steps"]: self.steps, self.domains["ingredients"]: self.ingredients}
            print(self.result_rules(values))

    def getRulesShare(self) -> list:
        values = {self.domains["steps"]: self.steps, self.domains["ingredients"]: self.ingredients}
        rulesShares = []
        for index, rule in enumerate(self.rules):
            strForRuleShare = "Rule" + str(index + 1) + ": " + str(rule(values))
            rulesShares.append(strForRuleShare)
        return rulesShares

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
