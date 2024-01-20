recipes = [
    {"name": "Spaghetti Carbonara", "ingredients": {"pasta", "bacon", "eggs", "parmesan"}},
    {"name": "Tomato Soup", "ingredients": {"tomato", "onion", "garlic", "broth"}},
    # Add more recipes here
]

user_input = input("Enter the ingredients you have, separated by commas: ")
user_ingredients = {ingredient.strip().lower() for ingredient in user_input.split(',')}


def find_matching_recipes(user_ingredients, recipes):
    matching_recipes = []
    for recipe in recipes:
        if recipe["ingredients"].issubset(user_ingredients):
            matching_recipes.append(recipe["name"])
    return matching_recipes

matched_recipes = find_matching_recipes(user_ingredients, recipes)


if matched_recipes:
    print("You can make the following recipes:")
    for recipe in matched_recipes:
        print(recipe)
else:
    print("No matching recipes found with the ingredients provided.")



def find_matching_recipes(user_ingredients, recipes):
    matching_recipes = []
    for recipe in recipes:
        if recipe["ingredients"].issubset(user_ingredients):
            matching_recipes.append(recipe["name"])
    return matching_recipes

# Sample recipes
recipes = [
    {"name": "Spaghetti Carbonara", "ingredients": {"pasta", "bacon", "eggs", "parmesan"}},
    {"name": "Tomato Soup", "ingredients": {"tomato", "onion", "garlic", "broth"}},
    # Add more recipes here
]

user_input = input("Enter the ingredients you have, separated by commas: ")
user_ingredients = {ingredient.strip().lower() for ingredient in user_input.split(',')}

matched_recipes = find_matching_recipes(user_ingredients, recipes)

if matched_recipes:
    print("You can make the following recipes:")
    for recipe in matched_recipes:
        print(recipe)
else:
    print("No matching recipes found with the ingredients provided.")


