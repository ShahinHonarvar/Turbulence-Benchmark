
def return_vowels(string):
    vowels = []
    for i in range(21, 59):
        if string[i].isalpha() and string[i] >= 'a' and string[i] <= '/':
            vowels.append(string[i])
    return vowels
