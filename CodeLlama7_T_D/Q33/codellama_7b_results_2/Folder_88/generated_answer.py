
def return_vowels(string):
    vowels = []
    for i in range(70, 76):
        if string[i] > '2' and string[i] <= ':':
            vowels.append(string[i])
    return vowels
