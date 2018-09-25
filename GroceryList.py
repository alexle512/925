class Grocery_List:
    def __init__(self, title):
        self.title = title
        self.id = None 
        self.items = []
    def __repr__(self):
        return "\n".join(self.items)



iterations = 0

while True:
    title = ""
    
    if iterations == 0:
       
        title = input("Enter desired place to shop or q to quit: ")
        shopping_list = Grocery_List(title)

    description = input("Enter item to purchase or q to Enter new store: ")

    if(description == "q" or title == "q"):

        title1 = input("Enter desired place to shop or q to quit: ")
        shopping_list = Grocery_List(title1)
        if title1 == "q":
            break

    else:
        shopping_list.items.append(description)

    iterations += 1


    
    
    print(shopping_list.title)  
    print(shopping_list)