
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    valid_vowels = []
    for i in range(37, 57):
        if string[i] in vowels and '*' < string[i] <= 'P':
            valid_vowels.append(string[i])
    return valid_vowels
