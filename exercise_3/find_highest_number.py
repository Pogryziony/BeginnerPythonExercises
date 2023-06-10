def find_highest_number():
    array = input("Enter numbers [splitted with ',']")
    array = array.split(",")
    number_of_errors = 0
    highest = int(array[0])
    for number in array[1:]:
        try:
            if int(number) > highest:
                highest = int(number)
        except ValueError:
            print("ERROR! Wrong type!", number)
            number_of_errors += 1
    print("Highest number in array is: ", highest)
    print("Number of type errors: ", number_of_errors)
    return highest
