
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sub_string = s[3:9]
    filtered_letters = [ch for ch in sub_string if ch in vowels and ch > 'S' and ch <= 'U']
    return filtered_letters
