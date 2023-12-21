 def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 19
    end_index = 20
    filtered_vowels = []
    for i in range(start_index, end_index):
        current_char = string[i]
        if current_char.isalpha():
            if current_char > '<' and current_char <= 'p':
                filtered_vowels.append(current_char)
    return filtered_vowels
