
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    filtered_chars = [char for char in s[202:872] if char in vowels and '3' < char <= '>']
    return filtered_chars
