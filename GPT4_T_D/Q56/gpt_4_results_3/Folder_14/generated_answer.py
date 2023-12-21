
def all_substring_of_size_n(string):
    output = []
    substring_size = 85
    for i in range(len(string)-substring_size+1):
        for j in range(i+substring_size,len(string)+1):
            substring = string[i:j]
            if len(set(substring))==len(substring):
                if substring not in output:
                    output.append(substring)
    return output
