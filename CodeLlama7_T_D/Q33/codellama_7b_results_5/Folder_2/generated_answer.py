
def return_vowels(string):
    vowels = []
    for i in range(170, 645):
        char = string[i]
        if char.isalpha() and char.lower() in 'aeiou':
            if char > 'E' and char <= '~':
                vowels.append(char)
    return vowels
