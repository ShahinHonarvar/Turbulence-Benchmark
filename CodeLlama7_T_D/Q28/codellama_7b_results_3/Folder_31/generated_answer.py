
def return_nth_smallest_ascii(string):
    # create a dictionary to store the character counts
    char_counts = {}

    # iterate through the string and increment the count for each character
    for char in string:
        if char in char_counts:
            char_counts[char] += 1

        else:
            char_counts[char] = 1

    # sort the dictionary by value in descending order
    sorted_dict = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    # return the character with the 18th smallest ASCII value
    for i, (char, count) in enumerate(sorted_dict):
        if i == 17:
            return char
