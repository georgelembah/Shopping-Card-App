shopping_list = []



def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see the items in your shopping card.
""")
    
def add_to_list(item):
  shopping_list.append(item)
  print (f" {item} has been added to ur list.")
  print("You have", len(shopping_list), "items" , "in your shopping cart")

    
def show_list():
  print("Here are the items in you list:")
  for items in shopping_list:
    print("* " , items)


show_help()
while True:
    new_item = input("> ")
    
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue   
    elif new_item == "SHOW":
      show_list()
      continue
      
      
    add_to_list(new_item)      
    
show_list()    
    