
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowel_list = [char for char in s[47:89] if char in vowels and char > '@' and char <= 'n']
    return vowel_list
