
def return_vowels(string):
    vowels = []
    for i in range(149, 313):
        if string[i].isalpha() and string[i].lower() in "aeiou" and string[i] > "m":
            vowels.append(string[i])
    return vowels
