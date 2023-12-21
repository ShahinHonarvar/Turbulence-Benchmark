
def if_contains_anagrams(str_list):
    # Create a dictionary to store the number of anagrams of each length
    anagram_dict = {}
    for str in str_list:
        # Convert the string to lowercase
        lowercase_str = str.lower()
        # Get the length of the string
        len_str = len(lowercase_str)
        # Check if the length is at least three
        if len_str >= 3:
            # Create a list of all possible anagrams of the string
            anagram_list = []
            for i in range(len_str - 2):
                for j in range(i + 1, len_str - 1)):
                    anagram_list.append(lowercase_str[i] + lowercase_str[j] + lowercase_str[k])
            # Check if any of the anagrams appear more than once in the list
            for anagram in anagram_list:
                if anagram_dict.get(anagram):
                    return False

                else:
                    anagram_dict[anagram] = True

    return True
