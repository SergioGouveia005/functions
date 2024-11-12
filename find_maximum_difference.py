def find_maximum_difference(a, b):
    # code implementation here...
    a_max = int(max(a))
    b_max = int(max(b))
    a_min = int(min(a))
    b_min = int(min(b))

    maximum = 0
    if a_max - b_min > b_max - a_min:
        maximum = a_max - b_min
    else:
        maximum = b_max - a_min
    return maximum

print(find_maximum_difference([1,5,600], [100,7,3,29,39])) #Outputs 597
print(find_maximum_difference([1,5,600], [100,7,3,602,39])) #Outputs 601


