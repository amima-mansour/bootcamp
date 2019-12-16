from book import Book
from recipe import Recipe
from datetime import datetime

Recipe_1 = Recipe('first', 2, 30, ['poivre', 'sel'], "blabla", 'dessert')
Recipe_2 = Recipe('second', 1, 30, ['poivre', 'sel'], "blabla", 'lunch')
Recipe_3 = Recipe('third', 5, 30, ['poivre', 'sel'], "blabla", 'starter')
recipe_dict = {}
recipe_dict['dessert'] = []
recipe_dict['lunch'] = []
recipe_dict['starter'] = []
recipe_dict['dessert'].append(Recipe_1)
recipe_dict['lunch'].append(Recipe_2)
recipe_dict['starter'].append(Recipe_3)
book = Book('My book', datetime.now(), datetime.now(), recipe_dict)
print(book.get_recipe_by_name('first'))
print(book.get_recipes_by_types('dessert'))
Recipe_4 = Recipe('four', 5, 60, ['poivre', 'sel'], "blabla", 'dessert')
book.add_recipe(Recipe_4)
print(book.get_recipes_by_types('dessert'))
update_string = book.last_update.strftime("%d/%m/%Y %H:%M:%S")
print(update_string)