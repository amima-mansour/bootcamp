class Recipe:
    """Class defying a recipe :
    - name
    - cooking_lvl
    - cooking_time
    - ingredients
    - description
    - recipe_type"""

    
    def __init__(self, name, lvl, minutes, ingredients, description, recipe_type):
        try:
            assert isinstance(name, str)
            self.name = name
            assert isinstance(lvl, int) and lvl < 6 and lvl > 0
            self.cooking_lvl = lvl
            assert isinstance(minutes, int) and minutes >= 0
            self.cooking_time = minutes
            assert isinstance(ingredients, list)
            test = [el for el in ingredients if not isinstance(el, str)]
            assert len(test) == 0
            self.ingredients = ingredients
            assert isinstance(description, str)      
            self.description = description
            assert recipe_type in ["starter", "lunch", "dessert"]
            self.recipe_type = recipe_type
        except:
            print("ERROR Recipe")
        

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = 'Recipe(name = '+ self.name + ', cooking_lvl = ' + str(self.cooking_lvl)\
            + ', cooking_time = ' + str(self.cooking_time) + 'min , ingredients = ' +\
            str(self.ingredients) + ', recipe_type = ' + self.recipe_type + ')'
        return txt