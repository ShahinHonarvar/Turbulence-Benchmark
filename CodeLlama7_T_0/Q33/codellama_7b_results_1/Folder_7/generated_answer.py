
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 202
    end_index = 872
    result = []
    for i in range(start_index, end_index + 1):
        if my_string[i].isalpha() and my_string[i] in vowels and my_string[i] > '3' and my_string[i] <= '8':
            result.append(my_string[i])
    return result
