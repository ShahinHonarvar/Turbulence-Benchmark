
def return_nth_smallest_ascii(string):
        # Convert the string to a list of characters
        char_list = list(string)
        # Initialize a dictionary to store the frequency of each character
        char_freq = {}
        # Iterate over the list of characters and increment the frequency count for each character
        for char in char_list:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
        # Sort the dictionary by value (frequency) and return the nth smallest ASCII value
        sorted_char_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
        nth_smallest_ascii = sorted_char_freq[5][0]
        return nth_smallest_ascii
