
def return_vowels(strng):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    return [char for char in strng[170:645] if char in vowels and 'E' < char <= '~']
