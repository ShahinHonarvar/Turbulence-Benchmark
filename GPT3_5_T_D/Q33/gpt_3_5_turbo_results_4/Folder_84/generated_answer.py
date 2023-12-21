
def return_vowels(string):
    vowels = []
    for letter in string[770:852]:
        if 'B' < letter <= 'i' and letter in 'aeiouAEIOU':
            vowels.append(letter)
    return vowels
