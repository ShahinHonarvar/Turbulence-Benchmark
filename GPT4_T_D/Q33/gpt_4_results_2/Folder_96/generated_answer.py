
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = [char for char in string[77:84] if char in vowels and '(' < char <= 'G']
    return result
