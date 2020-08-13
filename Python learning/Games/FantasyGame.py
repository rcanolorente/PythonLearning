inventory = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1} #had the numbers in strings so it was giving me a TypeError

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        print(value, ' ', key)
        item_total += int(value)
    print("Total number of items: "+str(item_total))


displayInventory(inventory)

def additems(inventory, newitems):
    for item in newitems:
        inventory.setdefault(item, 0)
        inventory[item] += 1 #need to add [item]


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

additems(inventory, dragonLoot)
displayInventory(inventory)