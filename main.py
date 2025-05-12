from data_structures.hashmap import HashMap


table = HashMap(100)
table.insert("One", 1)
table.insert("Two", 2)
table.insert("Three", 3)

print(table.get("One"))
print(table.get("Tww"))