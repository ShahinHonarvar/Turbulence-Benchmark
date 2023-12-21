
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[1:9] if char in vowels and '?' < char <= 'k']
    return result
