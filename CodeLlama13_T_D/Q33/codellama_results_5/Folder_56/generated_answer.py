
def return_vowels(string):
    vowels = []
    for char in string[15:86]:
        if char > '@' and char <= '~' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels
