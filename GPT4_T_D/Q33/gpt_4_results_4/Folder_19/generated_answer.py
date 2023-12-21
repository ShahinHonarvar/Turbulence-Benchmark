
def return_vowels(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    input_str = input_str[51:77]
    return [char for char in input_str if char in vowels and '4' < char <= '=']
