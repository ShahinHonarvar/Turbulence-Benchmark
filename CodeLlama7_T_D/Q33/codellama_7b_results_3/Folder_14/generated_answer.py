 def return_vowels(my_string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    start_index = 47
    end_index = 61
    if start_index >= len(my_string) or end_index > len(my_string):
        return []

    vowels_in_range = [char for char in my_string[start_index:end_index] if char.isalpha() and char.lower() in vowels and char > '9' and char <= 'O']
    return vowels_in_range
