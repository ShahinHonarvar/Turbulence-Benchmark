
def return_vowels(string):
    vowels = []
    for i in range(77, 84):
        if string[i].lower() in "aeiou":
            vowels.append(string[i])
    return vowels
