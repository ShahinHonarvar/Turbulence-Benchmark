
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 10
    end_index = 97
    filtered_chars = []

    for char in my_string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels and char > 'R' and char <= 'b':
            filtered_chars.append(char)

    return filtered_chars
