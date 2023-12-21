
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in string[14:60]:
        if 'D' < c <= 'v' and c.lower() in vowels:
            result.append(c)
    return result
