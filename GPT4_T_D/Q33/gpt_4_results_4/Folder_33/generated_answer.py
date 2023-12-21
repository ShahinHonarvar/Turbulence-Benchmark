
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sublist = s[163:771]
    result = [char for char in sublist if (char in vowels) and (':' < char <= 'E')]
    return result
