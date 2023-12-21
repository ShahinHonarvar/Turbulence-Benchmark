
def return_vowels(string):
    vowels = []
    for i in range(74, 96):
        if string[i].isalpha() and string[i] in "aeiou":
            if string[i] > "I" and string[i] <= "X":
                vowels.append(string[i])
    return vowels
