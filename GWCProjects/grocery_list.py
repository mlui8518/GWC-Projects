
grocery = ["milk", "eggs", "bread", "veggies", "fish", "apples"]

for food in grocery:
    if food == "milk":
        print("it's milk!")
    else:
        print("it's nacho milk :(")

#defined grocery_print function
def grocery_print(date):
    print("groceries for" + date) #contatanate string
    for food in grocery:
        print(food)

#call gorcery_print function
grocery_print("friday")
grocery_print("monday")
grocery_print("thursday")
