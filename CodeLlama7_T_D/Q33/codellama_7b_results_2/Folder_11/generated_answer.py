
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 29
    end_index = 73
    filtered_chars = []

    for char in string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels and char > '#' and char <= '(':
            filtered_chars.append(char)

    return filtered_chars
