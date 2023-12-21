
def return_vowels(string):
    vowels = []
    for i in range(323, 526):
        if string[i] in 'aeiouAEIOU' and '+' < string[i] <= ':':
            vowels.append(string[i])
    return vowels
