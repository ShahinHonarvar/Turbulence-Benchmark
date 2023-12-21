
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    range_start = max(29, string.index('#') + 1)
    range_end = min(73, string.index('.') + 1)

    return [char for char in string[range_start:range_end] if char in vowels]
