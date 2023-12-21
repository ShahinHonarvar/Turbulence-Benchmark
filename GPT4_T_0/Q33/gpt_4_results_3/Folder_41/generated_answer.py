
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [char for char in s[71:81] if char in vowels and '>' < char <= 'U']
    return result
