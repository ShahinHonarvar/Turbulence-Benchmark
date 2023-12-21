
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 10
    end_index = 83
    percent_char = "%"
    e_char = "e"

    # Check if the input string is valid
    if not my_string or len(my_string) < start_index:
        return []

    # Initialize an empty list to store the vowels
    vowel_list = []

    # Iterate over the characters in the input string
    for char in my_string[start_index:end_index]:

        # Check if the current character is a vowel
        if char in vowels:

            # Check if the current character is greater than the percent character and smaller than or equal to the e character
            if char > percent_char and char <= e_char:
                vowel_list.append(char)

    return vowel_list
