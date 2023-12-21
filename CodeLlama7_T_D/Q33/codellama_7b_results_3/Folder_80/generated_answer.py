
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 85
    end_index = 99
    result = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels and char > '/' and char <= 'n':
            result.append(char)

    return result
