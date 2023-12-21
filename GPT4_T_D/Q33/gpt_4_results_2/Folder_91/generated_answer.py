
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    return [char for char in string[4:8] if char in vowels and "P" < char <= "r"]
