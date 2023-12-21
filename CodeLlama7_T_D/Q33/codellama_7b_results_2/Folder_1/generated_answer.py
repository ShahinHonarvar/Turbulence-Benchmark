
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 24
    end_index = 64
    filtered_list = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels and char > 'F' and char <= 'h':
            filtered_list.append(char)
    return filtered_list
