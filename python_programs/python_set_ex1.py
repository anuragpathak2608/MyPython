#Frozen Sets : Frozen sets are immutable objects that only support methods and operators

Normal_set = set(['1', 'Anurag', '2', 'Pathak'])
print(Normal_set)

print("Adding element to the normal set")
Normal_set.add(3)
print(Normal_set)

frozen_set1 = frozenset(['1', 'Anurag', '2', 'Pathak', 'Pathak'])
print(frozen_set1)

