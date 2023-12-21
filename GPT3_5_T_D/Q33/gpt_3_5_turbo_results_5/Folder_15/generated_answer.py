
def return_vowels(string):
    vowels = []
    for char in string[5:6]:
        if 'a' < char <= '^' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels
