
def return_vowels(string):
    vowels = []
    for i in range(56, 68):
        if string[i].isalpha() and string[i].lower() in "aeiou" and string[i] > "m" and string[i] <= "x":
            vowels.append(string[i])
    return vowels
