
def return_vowels(string):
    vowels = []
    for index in range(3, 8):
        if string[index].isalpha() and 'A' < string[index] <= 'D':
            if string[index] in "AEIOUaeiou":
                vowels.append(string[index])
    return vowels
