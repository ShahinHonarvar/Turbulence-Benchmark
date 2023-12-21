
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    return [ch for ch in string[133:306] if ch > c and ch <= d and ch in vowels] if any(ch > c and ch <= d and ch in vowels for ch in string[133:306]) else []
