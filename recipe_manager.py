class Ingredient:
    def __init__(self, name):
        self.name = name


class Recipe:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.ingredients = [] 

    def add_ingredient(self, ingredient, quantity):
        ingredient_and_quantity = {'ingredient': ingredient, 'quantity': quantity}
        self.ingredients.append(ingredient_and_quantity)
    
    def remove_ingredient(self, ingredient, quantity):
        ingredient_and_quantity = {'ingredient': ingredient, 'quantity': quantity}
        self.ingredients.remove(ingredient_and_quantity)
    
    def display_recipe(self):
        print(f"Recipe: {self.name}")
        print(f"Description: {self.description}")
        print("Ingredients: ")
        for ingredient_and_quantity in self.ingredients:
            print(f"{ingredient_and_quantity['quantity']} {ingredient_and_quantity['ingredient'].name}")


class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def delete_recipe(self, recipe):
        self.recipes.remove(recipe)

    def display_all_recipes(self):
        if not self.recipes:
            print("No recipes available yet")
        else:
            for recipe in self.recipes:
                recipe.display_recipe()
                print("\n-------------------------\n")


# Example usage:
if __name__ == "__main__":
    # Creating ingredients
    egg = Ingredient("Egg")
    flour = Ingredient("Flour")
    sugar = Ingredient("Sugar")

    # Creating recipes
    pancakes = Recipe("Pancakes", "Delicious pancakes recipe")
    pancakes.add_ingredient(egg, "2")
    pancakes.add_ingredient(flour, "300g")
    pancakes.add_ingredient(sugar, "200g")

    cake = Recipe("Cake", "Yummy cake recipe")
    cake.add_ingredient(egg, "2")
    cake.add_ingredient(flour, "300g")
    cake.add_ingredient(sugar, "200g")

    # Creating a RecipeManager and adding recipes
    manager = RecipeManager()
    manager.add_recipe(pancakes)
    manager.add_recipe(cake)

    # Display all recipes
    manager.display_all_recipes()

    # Removing a recipe
    manager.delete_recipe(cake)

    # Display all recipes after removal
    manager.display_all_recipes()
