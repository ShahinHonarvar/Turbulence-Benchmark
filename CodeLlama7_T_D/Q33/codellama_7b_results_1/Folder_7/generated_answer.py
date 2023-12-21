
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(202, 872):
        if my_string[i].lower() in vowels and my_string[i] > '3' and my_string[i] <= '8':
            result.append(my_string[i])
    return result
