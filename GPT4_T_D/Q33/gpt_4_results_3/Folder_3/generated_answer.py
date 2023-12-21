
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [ch for ch in string[50:77] if ch in vowels and ch > '#' and ch <= 'r']
    return result
