def is_palindrome():
    text = input("Enter text: ")
    text = text.strip()
    text = text.lower()
    reversed_text = text[::-1]
    if text == reversed_text:
        print("Text you have entered is a palindrome")
        print("Text: " + text)
        print("Reversed text :" + reversed_text)
        return True
    else:
        print("Text is not a palindrome")
        print("Text: " + text)
        print("Reversed text :" + reversed_text)
        return False