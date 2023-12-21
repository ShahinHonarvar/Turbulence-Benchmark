
def return_vowels(string):
    vowels = []
    for i in range(24, 68):
        if string[i].isalpha() and string[i].lower() in "aeiou":
            if string[i].lower() > "f" and string[i].lower() <= "|":
                vowels.append(string[i])
    return vowels
