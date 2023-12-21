
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(64, 82):
        if chr(i) > 'P' and chr(i) <= 'z' and chr(i) in vowels:
            result.append(chr(i))
    return result
