def letter_occurrence(input_string):
    # complete function implementation...
    count = 0
    for letter in input_string:
        if letter == "a" or letter == "A":
            count += 1
    return count

print(letter_occurrence("Amazing")) #Outputs 2
print(letter_occurrence("Always aim ambitiously")) #Outputs 4