
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 273
    end_index = 275
    filtered_chars = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels:
            if char.lower() > 'a' and char.lower() <= 'o':
                filtered_chars.append(char)
    return filtered_chars
