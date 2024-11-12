def is_golden_number(n):
    # function implementation ...
    boolean = False
    for i in range(1, n):
        #print(f"{i}*{n-i} = {i * (n-i)}")
        if (i * (n-i)) % 1000 == 0:
            boolean = True
            break
    return boolean

print(is_golden_number(65)) #Returns True
print(is_golden_number(70)) #Returns True
print(is_golden_number(61)) #Returns False