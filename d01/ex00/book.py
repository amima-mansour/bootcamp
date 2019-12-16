from datetime import datetime
from recipe import Recipe


class Book:
    """Class defying a book :
    - name
    - last update
    - creation date
    - recipe list"""

    
    def __init__(self, name, update, date, recipe_dict):
        try:
            assert isinstance(name, str)
            self.name = name
            assert isinstance(update, datetime)
            self.last_update = update
            assert isinstance(date, datetime)
            self.creation_date = date
            assert isinstance(recipe_dict, dict) and len(recipe_dict.keys()) == 3
            keys = recipe_dict.keys()
            x = [key for key in keys if key not in ["starter", "lunch", "dessert"]]
            assert len(x) == 0
            self.recipes_list = recipe_dict
        except:
            print("ERROR Book")


    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for index, el in self.recipes_list.items():
            print(el)
            for recipe in el:
                if recipe.name == name:
                    return (recipe)
        print("RECIPE NOT FOUND")
        return None


    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in ["starter", "lunch", "dessert"]:
            return self.recipes_list[recipe_type]
        print("ERROR RECIPE TYPE")
        return None

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
