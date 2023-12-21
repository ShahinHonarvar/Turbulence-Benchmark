
def return_vowels(string):
    vowels = []
    for i in range(12, 39):
        if string[i].isalpha() and string[i].lower() in "aeiou":
            vowels.append(string[i])
    return vowels
