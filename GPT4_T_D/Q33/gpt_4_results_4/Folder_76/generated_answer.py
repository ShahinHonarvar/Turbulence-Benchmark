
def return_vowels(string):
    valid_letters = [char for char in "aeiouAEIOU" if "B" < char <= "t"]
    return [char for char in string[495:837] if char in valid_letters]
