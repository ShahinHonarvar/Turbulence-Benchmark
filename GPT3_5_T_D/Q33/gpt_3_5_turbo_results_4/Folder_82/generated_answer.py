
def return_vowels(string):
    vowels = []
    for index in range(86, 99):
        char = string[index]
        if char > 'E' and char <= 'r' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels
