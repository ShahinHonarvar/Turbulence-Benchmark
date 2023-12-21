 def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 12
    end_index = 39
    filtered_list = []
    for char in my_string[start_index:end_index]:
        if char in vowels and ord(char) > ord(";") and ord(char) <= ord("|"):
            filtered_list.append(char)
    return filtered_list
