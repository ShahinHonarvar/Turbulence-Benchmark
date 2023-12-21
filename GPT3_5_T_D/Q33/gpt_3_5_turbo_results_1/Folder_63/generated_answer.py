
def return_vowels(string):
    vowels = []
    for char in string[34:69]:
        if char > '_' and char <= 'o' and char.lower() in 'aeiou':
            vowels.append(char)
    return vowels
