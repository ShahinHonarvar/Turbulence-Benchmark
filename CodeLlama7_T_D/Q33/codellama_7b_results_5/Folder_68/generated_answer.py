
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 1
    end_index = 9
    filtered_list = []
    for char in string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels and char > '?':
            filtered_list.append(char)

    return filtered_list
