
def return_vowels(string):
    vowels = []
    for i in range(202, 872):
        if string[i].isalpha() and string[i].lower() in "aeiou" and ord(string[i]) > 3:
            vowels.append(string[i])
    return vowels
