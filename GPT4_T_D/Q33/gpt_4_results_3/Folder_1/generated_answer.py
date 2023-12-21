
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    limited_string = string[24:64]
    result = [ch for ch in limited_string if ch in vowels and 'F' < ch <= 'h']
    return result
