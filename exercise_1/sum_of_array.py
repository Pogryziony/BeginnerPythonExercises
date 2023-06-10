def sum_array():
    while True:
        elements = input("Enter array numbers: ")
        try:
            arr = elements.split(',')
            arr = [int(element) for element in arr]
            break
        except ValueError:
            print("ERROR! Wrong type!")
    sum_of_array = sum(arr)
    print(sum_of_array)
    return sum_of_array


class SumOfArray:
    pass