def find_largest_number():
    while True:
        try:
            numbers = input("Enter a numbers (separated with ','): ")
            numbers_list = numbers.split(",")
            array_of_numbers = [float(number) for number in numbers_list]
            largest_number = max(array_of_numbers)
            break
        except ValueError:
            print("Error! You have entered wrong type.")
    if largest_number % 1 == 0:
        print(int(largest_number))
    else:
        print(largest_number)
    return largest_number
