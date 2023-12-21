
def return_vowels(string):
    vowels = []
    for i in range(529, 828):
        if string[i].isalpha() and string[i].lower() >= 'u' and string[i].lower() <= 'l':
            vowels.append(string[i])
    return vowels
