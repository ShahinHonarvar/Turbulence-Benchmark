
def return_vowels(string):
    vowels = []
    for i in range(13, 37):
        if string[i].isalpha() and string[i].lower() in "aeiou":
            if ord(string[i]) > ord("Z"):
                vowels.append(string[i])
    return vowels
