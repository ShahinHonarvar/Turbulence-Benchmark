
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 323
    end_index = 526
    filtered_vowels = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels and char > '+' and char <= ':':
            filtered_vowels.append(char)
    return filtered_vowels
