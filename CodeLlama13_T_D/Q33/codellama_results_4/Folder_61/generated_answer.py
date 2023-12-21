
def return_vowels(string):
    vowels = []
    for i in range(1, 4):
        if string[i].lower() in "aeiou" and string[i] <= 'I':
            vowels.append(string[i])
    return vowels
