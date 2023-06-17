def analyze_text():
    text = input("Please enter your text for analysis: ")
    words = len(text.split(' '))
    chars = len(text)
    sentences = len(text.split('.')) - 1
    small_letters = 0
    big_letters = 0
    numbers = 0
    spaces = 0
    other_chars = 0

    for char in text:
        if char.islower():
            small_letters += 1
        elif char.isdigit():
            numbers += 1
        elif char.isupper():
            big_letters += 1
        elif char.isspace():
            spaces += 1
        else:
            other_chars += 1

    print(
        f"Words: {words}\n"
        f"Characters: {chars}\n"
        f"Sentences: {sentences}\n"
        f"Small letters: {small_letters}\n"
        f"Big letters: {big_letters}\n"
        f"Numbers: {numbers}\n"
        f"Spaces: {spaces}\n"
        f"Other characters: {other_chars}"
    )
