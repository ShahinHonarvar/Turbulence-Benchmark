
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = [char for char in string[86:99] if char in vowels and 'E' < char <= 'r']
    return result
