
def return_vowels(string):
    vowels = []
    for i in range(36, 56):
        char = string[i]
        if char in "aeiou" and char > '+' and char <= '/':
            vowels.append(char)
    return vowels
