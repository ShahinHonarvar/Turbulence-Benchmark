
def return_vowels(string):
    vowels = []
    for i in range(20, 34):
        if string[i].isalpha() and string[i].lower() >= 'u' and string[i].lower() <= 'i':
            vowels.append(string[i])
    return vowels
