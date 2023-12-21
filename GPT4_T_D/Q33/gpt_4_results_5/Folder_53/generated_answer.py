
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    valid_chars = [char for char in string[27:57] if char in vowels and "o" < char <= "w"]
    return valid_chars
