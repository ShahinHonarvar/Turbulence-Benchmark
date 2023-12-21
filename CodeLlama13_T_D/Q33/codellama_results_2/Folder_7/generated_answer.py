
def return_vowels(string):
    vowels = []
    for i in range(202, 873):
        if string[i].isalpha() and ord(string[i]) > 3 and ord(string[i]) <= 872:
            vowels.append(string[i])
    return vowels
