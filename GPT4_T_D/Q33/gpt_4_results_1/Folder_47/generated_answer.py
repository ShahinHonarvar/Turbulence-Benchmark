
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    string = string[23:38]
    result = [char for char in string if char in vowels and 'N' < char <= 'k']
    return result
