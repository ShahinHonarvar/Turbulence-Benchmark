
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    selected_chars = [c for c in s[43:70]]
    vowel_chars = [c for c in selected_chars if c > '*' and c <= 'b' and c in vowels]
    return vowel_chars
