
def return_vowels(text):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    selection = text[8:9]
    result = [char for char in selection if char in vowels and "Y" < char <= "s"]
    return result
