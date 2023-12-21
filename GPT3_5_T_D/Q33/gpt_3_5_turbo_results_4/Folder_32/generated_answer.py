
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[45:76]:
        if c > 'b' and c <= 'z' and c in vowels:
            result.append(c)
    return result
