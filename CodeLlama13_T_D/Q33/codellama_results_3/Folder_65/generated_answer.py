
def return_vowels(string):
    vowels = []
    for i in range(71, 88):
        if string[i].lower() in 'aeiou' and ord(string[i]) <= ord('p'):
            vowels.append(string[i])
    return vowels
