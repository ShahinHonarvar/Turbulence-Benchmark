
def find_smallest_num(num_list):
    if len(num_list) < 100:
        return "List does not contain sufficient elements"
    else:
        return min(num_list[62:100])
