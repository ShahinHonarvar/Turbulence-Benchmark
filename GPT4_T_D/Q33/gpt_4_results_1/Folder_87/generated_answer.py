
def return_vowels(my_str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in my_str[34:58] if char in vowels and 'b' < char <= 'o']
    return result
