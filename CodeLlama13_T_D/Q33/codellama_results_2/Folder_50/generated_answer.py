
def return_vowels(string):
    vowels = []
    for i in range(11, 53):
        char = string[i]
        if "A" <= char <= "W":
            vowels.append(char)
    return vowels
