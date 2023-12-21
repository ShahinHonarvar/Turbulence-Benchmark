
def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[1:7] if char in vowels and 'F' < char <= 'j']
    return result
