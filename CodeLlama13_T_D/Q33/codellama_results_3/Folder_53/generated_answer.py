
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    return [c for c in string[27:57] if c in vowels and c > "o" and c <= "w"]
