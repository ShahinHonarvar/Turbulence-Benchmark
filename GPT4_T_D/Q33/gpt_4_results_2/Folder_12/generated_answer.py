
def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for c in s[13:37]:
        if c in vowels and 'Z' < c <= '}':
            result.append(c)
    return result
