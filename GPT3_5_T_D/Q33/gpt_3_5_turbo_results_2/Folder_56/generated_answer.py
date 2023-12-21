
def return_vowels(string):
    vowels = []
    for char in string[15:86]:
        if char > '@' and char <= '~' and char.lower() in 'aeiou':
            vowels.append(char)
    return vowels
