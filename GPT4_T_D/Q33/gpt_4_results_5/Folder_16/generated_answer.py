
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
    part = string[133: 306]
    result = [c for c in part if c in vowels and c > 'c' and c <= 'd']
    return result
