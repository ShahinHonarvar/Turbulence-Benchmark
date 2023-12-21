
def return_vowels(my_str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in my_str[44:95] if char in vowels and '5' < char <= '<']
    return result
