
def return_vowels(string):
    vowels = []
    for i in range(328, 456):
        if string[i].isalpha() and string[i] > '<' and string[i] <= 'z':
            vowels.append(string[i])
    return vowels
