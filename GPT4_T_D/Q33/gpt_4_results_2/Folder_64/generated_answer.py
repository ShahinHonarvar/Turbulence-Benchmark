
def return_vowels(input_str):
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sub_string = input_str[1:7]
    resultant_list = [char for char in sub_string if char in vowel_list and 'F' < char <= 'j']
    return resultant_list
