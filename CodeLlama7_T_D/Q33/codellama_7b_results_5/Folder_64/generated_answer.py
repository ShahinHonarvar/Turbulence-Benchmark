 def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(1, len(my_string)):
        if my_string[i].lower() in vowels and my_string[i] > 'f' and my_string[i] <= 'j':
            result.append(my_string[i])
    return result
