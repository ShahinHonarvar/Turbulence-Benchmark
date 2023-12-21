
def return_vowels(s):
    sub_str = s[171:402]
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in sub_str if char in vowels and char > 'I' and char <= 'k']
    return result
