
def return_vowels(string):
    vowels = set("aeiouAEIOU")
    filtered_chars = [char for char in string[11:61] if char in vowels and "M" < char <= "W"]
    return filtered_chars
