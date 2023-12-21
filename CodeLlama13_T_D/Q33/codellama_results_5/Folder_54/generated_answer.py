
def return_vowels(string):
    vowels = []
    for i in range(23, 85):
        if string[i].isalpha() and string[i].upper() >= "W" and string[i].lower() <= "v":
            vowels.append(string[i])
    return vowels
