
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    valid_vowels = []
    for index in range(17, 65):
        if string[index] in vowels and string[index] > 'U' and string[index] <= '{':
            valid_vowels.append(string[index])
    return valid_vowels
