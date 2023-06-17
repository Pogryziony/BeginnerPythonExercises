def fibonacci_sequence(number):
    fibonacci_seq = [0, 1]
    for i in range(2, number):
        next_element = fibonacci_seq[i - 1] + fibonacci_seq[i - 2]
        fibonacci_seq.append(next_element)
    print(fibonacci_seq[:number])
