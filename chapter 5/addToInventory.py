List to Dictionary Function for Fantasy Game Inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v,k)
        item_total+=int(v)
        
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for itemName in addedItems:
        inventory.setdefault(itemName,0)
        inventory[itemName]+=1
    return(inventory)
            
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

