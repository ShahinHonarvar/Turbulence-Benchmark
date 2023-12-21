
def return_n_greatest_chars(char_string):
    char_code_list = [ord(char) for char in char_string]
    char_code_list.sort(reverse=True)
    greatest_chars = char_code_list[:72]
    greatest_chars.sort()
    return [chr(char_code) for char_code in greatest_chars]
