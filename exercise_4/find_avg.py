def find_avg():
    array = input("Enter numbers [split with ',']: ")
    array = array.split(",")
    second_array = []
    for number in array:
        second_array.append(float(number))
    sum_of_array = sum(second_array)
    avg = sum_of_array / len(second_array)
    print("Average:", avg)
