
def return_vowels(string):
    vowels = []
    for char in string[170:645]:
        if char.isalpha() and char.islower() and char > 'E' and char <= '~':
            if char in 'aeiou':
                vowels.append(char)
    return vowels
