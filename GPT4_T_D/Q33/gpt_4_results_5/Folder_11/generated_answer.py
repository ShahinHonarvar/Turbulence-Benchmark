
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    portion = string[29:73]
    valid_chars = [char for char in portion if char > "#" and char <= "(" and char.lower() in vowels]
    return valid_chars
