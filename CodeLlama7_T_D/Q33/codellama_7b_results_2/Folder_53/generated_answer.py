
def return_vowels(string):
    vowels = []
    for i in range(27, 57):
        if string[i].lower() == 'a' or string[i].lower() == 'e' or string[i].lower() == 'i' or string[i].lower() == 'o' or string[i].lower() == 'u':
            vowels.append(string[i])
    return vowels
