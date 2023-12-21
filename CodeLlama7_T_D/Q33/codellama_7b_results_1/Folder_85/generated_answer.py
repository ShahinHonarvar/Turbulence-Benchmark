
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 55
    end_index = 65
    filtered_vowels = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels and char > 'Z' and char <= 'w':
            filtered_vowels.append(char)
    return filtered_vowels
