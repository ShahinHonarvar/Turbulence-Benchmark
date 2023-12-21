
def return_vowels(string):
    vowels = []
    for letter in string[71:88]:
        if '9' < letter <= 'P' and letter in 'AEIOUaeiou':
            vowels.append(letter)
    return vowels
