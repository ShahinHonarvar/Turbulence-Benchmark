def find_original_set(arg):
    return {i:j for i in range(len(arg), -1, -1) for j in range(len(arg[i]))}
