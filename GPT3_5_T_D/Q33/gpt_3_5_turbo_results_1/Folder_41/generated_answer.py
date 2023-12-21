
def return_vowels(string):
    vowels = []
    for char in string[71:81]:
        if '>' < char <= 'U' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels
