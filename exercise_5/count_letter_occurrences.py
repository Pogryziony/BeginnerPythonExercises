def count_letter_occurrences():
    text = input("Enter text: ")
    dictionary = {}
    for character in text:
        if character.isalpha():
            character = character.lower()
            dictionary[character] = dictionary.get(character, 0) + 1
    print("Occurrences of each letter:")
    for char, count in dictionary.items():
        print(char, ":", count)
    return dictionary

