
def palindrome_checker(word):
    reverse_word = word[::-1]
    if word == reverse_word:
         print("this is a palindrome")
    else: print("this is not a palindrome")
    
for i in range(10):
    word = input("enter a word ")
    palindrome_checker(word)


