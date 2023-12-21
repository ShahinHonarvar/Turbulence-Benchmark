 def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 37
    end_index = 57
    result = []
    for i in range(start_index, end_index + 1):
        current_char = my_string[i]
        if current_char > '*' and current_char <= 'P':
            if current_char in vowels:
                result.append(current_char)
    return result
