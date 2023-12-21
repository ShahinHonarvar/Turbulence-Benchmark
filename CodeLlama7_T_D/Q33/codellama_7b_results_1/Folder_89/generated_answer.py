
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 50
    end_index = 51
    result = []
    for char in my_string[start_index:end_index]:
        if char in vowels and char > ',' and char <= 'v':
            result.append(char)
    return result
