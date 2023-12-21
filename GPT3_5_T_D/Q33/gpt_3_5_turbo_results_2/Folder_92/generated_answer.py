
def return_vowels(string):
    vowels = []
    for char in string[3:8]:
        if char > ';' and char <= 'D' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels
