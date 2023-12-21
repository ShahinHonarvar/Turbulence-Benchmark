
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    return [char for char in string[10:97] if char in vowels and 'R' < char <= 'b']
