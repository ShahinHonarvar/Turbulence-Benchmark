
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s = s[71:88]
    return [char for char in s if char in vowels and '9' < char <= 'P']
