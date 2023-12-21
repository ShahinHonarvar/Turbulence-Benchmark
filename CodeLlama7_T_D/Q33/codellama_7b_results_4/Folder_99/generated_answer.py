
def return_vowels(string):
    vowels = []
    for i in range(323, 526):
        if string[i].isalpha() and string[i] in "aeiou":
            vowels.append(string[i])
    return vowels
