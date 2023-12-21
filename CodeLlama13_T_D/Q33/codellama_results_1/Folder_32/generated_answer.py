
def return_vowels(string):
    vowels = []
    for i in range(45, 76):
        if string[i].lower() in "aeiou" and string[i].lower() >= "b" and string[i].lower() <= "z":
            vowels.append(string[i])
    return vowels
