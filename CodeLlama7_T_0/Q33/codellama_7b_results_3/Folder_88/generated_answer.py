
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 70
    end_index = 76
    result = []
    for i in range(start_index, end_index + 1):
        if my_string[i] in vowels and my_string[i] > '2' and my_string[i] <= ':':
            result.append(my_string[i])
    return result
