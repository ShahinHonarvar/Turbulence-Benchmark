
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    string_section = string[14:60]
    filter_vowels = [char for char in string_section if char in vowels and 'D' < char <= 'v']
    return filter_vowels
