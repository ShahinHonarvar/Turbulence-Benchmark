
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    filtered = [char for char in string[12:39] if char > ';' and char <= '|']
    return [char for char in filtered if char in vowels]
