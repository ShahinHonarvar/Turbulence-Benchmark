
def return_vowels(string):
    vowels = []
    for i in range(21, 59):
        if string[i] > '/' and string[i] <= 'a' and string[i] in 'aeiou':
            vowels.append(string[i])
    return vowels
