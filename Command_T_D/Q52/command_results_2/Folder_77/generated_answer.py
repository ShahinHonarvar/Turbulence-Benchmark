def palindrome_of_length_n(s):
    return set(s.lower().replace(" ","").replace("'","").replace(" ","").split("'").split(" ")[::-1])
