print("Welcome to the GREAT Palindrome checker, not sure if your word is a palindrome??? Come check it here!!! \n")

def palindrome_checker(word):
    word = word.lower()
    reverse_word = word[::-1]
    if word == reverse_word:
         print("this is a palindrome \n")
    else: print("this is not a palindrome \n")
    
print("*devnote: write 'quit' to quit the program \n")
while True:
    word = input("Please enter in a word to check ")
    if word == "quit":
        print("the program has stopped \n")
        break
    palindrome_checker(word)
    
