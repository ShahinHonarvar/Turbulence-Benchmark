
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 273
    end_index = 275
    matched_chars = []

    for char in string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels and char > '+' and char <= 'o':
            matched_chars.append(char)

    return matched_chars
