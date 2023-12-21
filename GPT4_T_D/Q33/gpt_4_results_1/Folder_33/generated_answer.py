
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    valid_chars = [chr(i) for i in range(ord(':')+1, ord('E')+1)]
    result = [c for c in s[163:771] if c in vowels and c in valid_chars]
    return result
