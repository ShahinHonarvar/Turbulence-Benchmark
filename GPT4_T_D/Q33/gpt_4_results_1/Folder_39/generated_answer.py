
def return_vowels(string):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    string = string[32:97]
    return [ch for ch in string if (ch in vowels and "Q" < ch <= "]")]
