recipes = {
    'sandwich': {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": "10"},
    'cake': {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": "60"},
    'salad': {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": "15"}
    }


def print_recipe(recipe):
    print('Recipe for {}:'.format(recipe))
    recipe = recipes[recipe]
    print('Ingredients list: {}'.format(recipe['ingredients']))
    print("To be eaten for {}.".format(recipe['meal']))
    print('Takes {} minutes of cooking.'.format(recipe['prep_time']))


def delete_recipe(recipe):
    del recipes[recipe]


def add_recipe(recipe_name, ingredients, meal, prep_time):
    recipe = {}
    recipe['ingredients'] = ingredients
    recipe['meal'] = meal
    recipe['prep_time'] = prep_time
    recipes[recipe_name] = recipe


def print_cookbook():
    for el in recipes.keys():
        print_recipe(el)


while True:
    answer = input('Please select an option by typing the corresponding number\
        :\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n\
        4: Print the cookbook\n5: Quit\n')
    if answer == '5':
        print('Cookbook closed.')
        break
    if answer == '3':
        recipe = input("Please enter the recipe's name to get its details:\n")
        if recipe in recipes.keys():
            print_recipe(recipe)
        else:
            print('ERROR: Recipe not found')
    elif answer == '1':
        recipe_name = input('Please enter the name of the recipe\n')
        ingredients = []
        ingred = input('Please enter an ingredient or press q to quit\n')
        while ingred != 'q':
            ingredients.append(ingred)
            ingred = input('Please enter an ingredient or press q to quit\n')
        meal = input('Please enter the type of the meal\n[dessert, \
            lunch, breakfast, dinner]> ')
        prep_time = input('Please enter the preparation time\n')
        add_recipe(recipe_name, ingredients, meal, prep_time)
    elif answer == '4':
        print_cookbook()
    elif answer == '2':
        recipe = input("Please enter the recipe's name to delete:\n")
        if recipe in recipes.keys():
            delete_recipe(recipe)
        else:
            print('ERROR: Recipe not found')
    else:
        print('This option does not exist, please type the \
            corresponding number.')
        print('To exit, enter 5.')
