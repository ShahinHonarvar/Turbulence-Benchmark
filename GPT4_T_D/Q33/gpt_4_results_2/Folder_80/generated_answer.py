
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s = s[85:99]
    result = [char for char in s if char in vowels and char > '/' and char <= 'n']
    return result
