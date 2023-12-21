
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sliced_string = string[20:43]
    return [char for char in sliced_string if char in vowels and '5' < char <= 'M']
