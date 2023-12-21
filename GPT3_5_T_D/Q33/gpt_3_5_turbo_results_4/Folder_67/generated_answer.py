
def return_vowels(string):
    vowels = [ch for ch in string[21:59] if ch > '/' and ch <= 'a' and ch in 'aeiouAEIOU']
    return vowels if vowels else []
