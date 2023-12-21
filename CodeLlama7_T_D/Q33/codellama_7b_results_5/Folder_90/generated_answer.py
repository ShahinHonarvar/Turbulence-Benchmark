
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 142
    end_index = 145
    filtered_list = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels and char > '4' and char <= 'o':
            filtered_list.append(char)
    return filtered_list
