
def return_vowels(string):
    vowels = []
    for c in string:
        if ord(c) >= 65 and ord(c) <= 70 and c != '%':
            vowels.append(c)
    return vowels
