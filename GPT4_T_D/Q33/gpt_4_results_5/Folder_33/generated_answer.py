
def return_vowels(string):
    subset_str = string[163:771]
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    selected_chars = [ch for ch in subset_str if ch > ':' and ch <= 'E' and ch in vowels]
    return selected_chars
