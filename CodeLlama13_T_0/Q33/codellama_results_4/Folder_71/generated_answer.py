
def return_vowels(string):
    vowels = []
    for i in range(36, 57):
        if string[i].isalpha() and string[i].lower() in "aeiou":
            vowels.append(string[i])
    return vowels
