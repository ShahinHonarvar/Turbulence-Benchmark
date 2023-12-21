
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for ch in s[86:99]:
        if ch.lower() in vowels and 'e' < ch.lower() <= 'r':
            result.append(ch)
    return result
