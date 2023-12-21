
def filter_chars(string):
    start = 2
    end = 7
    filtered_string = ""
    
    for i in range(len(string)):
        if start <= i < end:
            if "h" < string[i] < "k":
                continue
        filtered_string += string[i]
    
    return filtered_string
