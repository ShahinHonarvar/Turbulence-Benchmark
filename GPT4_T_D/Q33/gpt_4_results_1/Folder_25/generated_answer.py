
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [char for char in string[28:76] if char in vowels and 
                       ord(char) > ord('+') and ord(char) <= ord('z')]
    return filtered_vowels
