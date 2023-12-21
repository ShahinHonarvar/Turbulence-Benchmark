
def all_substring_of_size_n(input_string):
    output_list = []
    for i in range(len(input_string) - 78):
        substr = input_string[i:i+79]
        if len(set(substr)) == len(substr):
            output_list.append(substr)
    return list(set(output_list))
