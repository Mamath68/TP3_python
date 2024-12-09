def is_palindrome(s):
    word = s.lower()
    cleaned_word = ''.join(clean for clean in word if clean.isalpha())
    print(cleaned_word)
    return cleaned_word == cleaned_word[::-1]

def main():
    user_input = input("Entrez un mot ou une phrase : ")
    if is_palindrome(user_input):
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")

if __name__ == "__main__":
    main()
