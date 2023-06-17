def analyze_text():
    text = input("Please enter your text for analysis: ")
    words = len(text.split(' '))
    chars = len(text)
    sentences = len(text.split('.')) - 1
    small_letters = sum(1 for char in text if char.islower())
    big_letters = sum(1 for char in text if char.isupper())
    numbers = sum(1 for char in text if char.isnumeric())
    spaces = sum(1 for char in text if char.isspace())
    other_chars = sum(1 for char in text if not char.isalnum() and not char.isspace())

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
