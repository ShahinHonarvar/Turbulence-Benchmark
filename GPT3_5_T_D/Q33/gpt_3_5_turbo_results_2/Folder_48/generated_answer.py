
def return_vowels(string):
    vowels = []
    for i in range(529, 828):
        char = string[i]
        if char > 'U' and char <= 'l' and char.lower() in 'aeiou':
            vowels.append(char)
    return vowels
