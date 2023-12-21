
def return_vowels(string):
    vowels = []
    for i in range(464, 574):
        if string[i].isalpha() and string[i].lower() in "aeiou":
            if string[i] > "a" and string[i] <= "g":
                vowels.append(string[i])
    return vowels
