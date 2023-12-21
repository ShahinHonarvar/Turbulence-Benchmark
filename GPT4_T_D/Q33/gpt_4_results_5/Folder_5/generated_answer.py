
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    string = string[44:95]
    return [char for char in string if char in vowels and '5' < char <= '<']
