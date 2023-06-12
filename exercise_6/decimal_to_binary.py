def decimal_to_binary():
    while True:
        try:
            decimal = int(input("Enter a number: "))
            binary = bin(decimal)[2:]
            break
        except ValueError:
            print("ERROR! Invalid input. Please enter an integer.")
    print("Decimal:", decimal)
    print("Binary:", binary)
    return binary
