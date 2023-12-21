
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for ch in string[34:58]:
        if ch in vowels and 'b' < ch <= 'o':
            result.append(ch)
    return result
