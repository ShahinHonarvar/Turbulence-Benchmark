
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 63):
        substring = s[i:i+64]
        if substring == substring[::-1] and all(character.isalpha() for character in substring):
            result.add(substring)
    return result
