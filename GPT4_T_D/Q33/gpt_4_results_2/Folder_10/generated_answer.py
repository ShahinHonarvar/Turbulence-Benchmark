
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    return [char for char in string[31:37] if char in vowels and ";" < char <= "t"]
