
def return_vowels(string):
    vowels = []
    for i in range(60, 99):
        if string[i].lower() in "aeiou":
            vowels.append(string[i])
    return vowels
