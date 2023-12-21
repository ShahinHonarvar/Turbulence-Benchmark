
def return_vowels(string):
    vowels = []
    for i in range(1, 7):
        if string[i].isalpha() and string[i].lower() in "aeiou":
            vowels.append(string[i])
    return vowels
