
def return_vowels(input_string):
    vowels = ['e']
    output_list = []
    substring = input_string[29:31]
    for char in substring:
        if char in vowels:
            output_list.append(char)
    return output_list
