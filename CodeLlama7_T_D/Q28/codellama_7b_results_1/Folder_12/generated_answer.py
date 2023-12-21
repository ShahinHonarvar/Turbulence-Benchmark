
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Sort the dictionary by value in descending order
    sorted_dict = dict(sorted(char_freq.items(), key=lambda x: x[1], reverse=True))
    # Get the top 5 most frequent characters and their frequencies
    top_5 = []
    for i in range(5):
        if len(top_5) < 5:
            top_5.append((sorted_dict.keys()[i], sorted_dict.values()[i]))
        else:
            break

    # Return the character with the 5th smallest ASCII value among those characters in the string that occur between indices 3 to 26, both inclusive
    return top_5[4][0]
