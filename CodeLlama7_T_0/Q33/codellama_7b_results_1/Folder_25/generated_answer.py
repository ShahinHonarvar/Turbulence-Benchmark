
def return_vowels(string):
    vowels = []
    for i in range(28, 76):
        if string[i].isalpha() and string[i].lower() in "aeiou":
            if string[i] > "+":
                if string[i] <= "z":
                    vowels.append(string[i])
    return vowels
