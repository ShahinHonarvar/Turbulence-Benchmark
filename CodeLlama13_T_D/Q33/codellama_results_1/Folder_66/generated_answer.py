
def return_vowels(string):
    vowels = []
    for i in range(63, 79):
        if string[i].isalpha() and string[i] > "D" and string[i] <= "y":
            vowels.append(string[i])
    return vowels
