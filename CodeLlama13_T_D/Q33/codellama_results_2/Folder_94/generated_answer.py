
def return_vowels(string):
    vowels = []
    for i in range(40, 95):
        if string[i].isalpha() and string[i].lower() in "aeiou" and ord(string[i]) > 4 and ord(string[i]) <= ord("H"):
            vowels.append(string[i])
    return vowels
