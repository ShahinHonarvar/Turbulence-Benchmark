
def return_vowels(string):
    vowels = []
    for i in range(14, 60):
        if string[i].lower() in "aeiou":
            if string[i].lower() > "d" and string[i].lower() <= "v":
                vowels.append(string[i])
    return vowels
