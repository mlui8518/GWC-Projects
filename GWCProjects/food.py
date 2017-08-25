Ingredients = {"Salt":"a pinch", "Vegetable Oil":"a drizzle", "Elbow Macaroni or Cavatappi":"1 pound", "Milk":"1 quart", "Unsalted Butter, Divided":"8 teaspoons (1 stick)", "All-Purpose Flour":"1/2 cup", "Gruyere, grated":"12 ounces (4 cups)", "Cheddar, grated":"8 ounces (2 cups)", "Grounded Black Pepper":"1/2 teaspoon", "Ground Nutmeg":"1/2 teaspoon", "Tomatoes":"3/4 pound (4 small)", "White Bread Crumbs":"1 1/2 cups (5 slices, crusts removed)"}

directions_list = ['Preheat the oven to 375 degrees F.', 'Drizzle oil into a large pot of boiling salted water. Add the macaroni and cook according to the directions on the package, 6 to 8 minutes. Drain well.', 'Heat the milk in a small saucepan, but do not boil it.', 'Melt 6 tablespoons of butter in a large (4-quart) pot and add the flour. Cook over low heat for 2 minutes, stirring with a whisk. While whisking, add the hot milk and cook for a minute or two more, until thickened and smooth.', 'Off the heat, add the Gruyere, Cheddar, 1 tablespoon salt, pepper, and nutmeg.', 'Add the cooked macaroni and stir well.', 'Pour into a 3-quart baking dish.', 'Slice the tomatoes and arrange on top.', 'Melt the remaining 2 tablespoons of butter, combine them with the fresh bread crumbs, and sprinkle on the top.', 'Bake for 30 to 35 minutes, or until the sauce is bubbly and the macaroni is browned on the top.']

print("Macaroni and Cheese Recipe")

print(Ingredients)


for i in directions_list:
	print("Next Step?")
	answer = input()
	if answer == "yes":
		print(i)
	else:
		exit()
		