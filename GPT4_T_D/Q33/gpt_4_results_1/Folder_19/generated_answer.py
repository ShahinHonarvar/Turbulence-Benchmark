
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    subset = s[51:77]
    return [char for char in subset if char in vowels and '4' < char <= '=']
