
def return_vowels(string):
    vowels = []
    for i in range(40, 91):
        if chr(i) > 'A' and chr(i) <= 'x' and chr(i) in 'aeiouAEIOU':
            vowels.append(chr(i))
    return vowels
