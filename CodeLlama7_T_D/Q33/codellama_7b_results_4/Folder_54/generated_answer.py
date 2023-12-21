
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 23
    end_index = 85
    result = []
    for char in my_string[start_index:end_index]:
        if char.isalpha():
            if vowels.count(char) > 0 and char > 'W' and char <= 'v':
                result.append(char)
    return result
