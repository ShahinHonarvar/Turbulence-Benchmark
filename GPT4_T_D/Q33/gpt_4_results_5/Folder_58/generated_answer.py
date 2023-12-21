
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    valid_chars = []
    for char in s[260:322]:
        if char in vowels and char > '%' and char <= 'U':
            valid_chars.append(char)
    return valid_chars
