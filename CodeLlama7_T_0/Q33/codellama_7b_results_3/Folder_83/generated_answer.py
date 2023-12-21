
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 90
    end_index = 97
    result = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels and char > '_' and char <= 'x':
            result.append(char)
    return result
