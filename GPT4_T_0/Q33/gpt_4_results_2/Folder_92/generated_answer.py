
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    return [char for char in s[3:8] if char in vowels and ';' < char <= 'D']
