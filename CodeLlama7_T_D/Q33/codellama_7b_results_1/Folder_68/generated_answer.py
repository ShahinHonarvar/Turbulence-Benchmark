
def return_vowels(string):
    vowels = []
    for i in range(1, 9):
        if string[i].isalpha() and string[i].lower() in "aeiou":
            if string[i].lower() > '?':
                if string[i].lower() <= 'k':
                    vowels.append(string[i])
    return vowels
