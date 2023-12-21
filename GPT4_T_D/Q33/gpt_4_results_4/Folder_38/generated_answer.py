
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = [ch for ch in string[17:65] if ch in vowels and 'U' < ch <= '{']
    return result
