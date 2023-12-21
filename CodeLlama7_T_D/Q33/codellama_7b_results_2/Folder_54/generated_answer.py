
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 23
    end_index = 85
    filtered_chars = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels and char > 'W' and char <= 'v':
            filtered_chars.append(char)
    return filtered_chars
