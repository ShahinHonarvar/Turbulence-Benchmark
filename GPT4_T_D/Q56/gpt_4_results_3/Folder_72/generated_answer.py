
def all_substring_of_size_n(s):
    substring_list=[]
    for i in range(len(s)):
        if i+88<=len(s) and len(set(s[i:i+88]))==88:
            substring_list.append(s[i:i+88])
    return list(set(substring_list))
