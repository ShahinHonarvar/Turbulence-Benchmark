
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sub_str = string[11:53]
    return [char for char in sub_str if char in vowels and '+' < char <= 'W']
