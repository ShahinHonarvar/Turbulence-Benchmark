
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    greater_than_F = [chr(i) for i in range(ord('F')+1, ord('h')+1)]
    selected_chars = [char for char in s[24:64] if char in vowels and char in greater_than_F]
    return selected_chars
