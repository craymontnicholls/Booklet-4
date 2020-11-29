def Exists(item, inventory):

  x = inventory.find("Sword")

  if x != -1:
    print("has sword")
  
  x = inventory.find("Shield")
  

  if x != -1:
    print("has Shield")

  x = inventory.find("Bow")

  if x != -1:
    print("has Bow")







items = "Sword , Shield, Bow"
inventory = "Sword , Bow"

Exists(items, inventory)