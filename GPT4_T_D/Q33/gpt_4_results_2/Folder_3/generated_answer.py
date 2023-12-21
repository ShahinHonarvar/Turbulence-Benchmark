
def return_vowels(string):
    vowels = "aeiouAEIOU"
    qualified_chars = [char for char in string[50:77] if char > "#" and char <= "r" and char in vowels]
    return qualified_chars
