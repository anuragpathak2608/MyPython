datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]

for element in datalist:
    Data_type = type(element)
    print("Element:", element, "\t\tType: ", Data_type)
