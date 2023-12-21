
def if_decimal_is_divisible(binary_string):
    def get_fibonacci():
        fibonacci_sequence = [0, 1]

        while len(fibonacci_sequence) < 15:
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
            
        return fibonacci_sequence[-1]
    
    decimal = int(binary_string, 2)
    
    return decimal % get_fibonacci() == 0
