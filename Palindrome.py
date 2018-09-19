
def backwards(word):
        return word[::-1]

def palindrome(word):
        pal = backwards(word)
        if (word == pal):
            return True
        return False

while True:
    word = input("Please enter word: ")
        
    answer = palindrome(word)

    if answer == True:
        print(word,"=",backwards(word), "-> This is a Palindrome")
    elif answer == False:
        print(word,"=",backwards(word), "-> This is not a Palindrome")

    go_again = input("Press (N) to exit or (Y) to continue: ")
    if go_again == "N":
        break
    else:
        continue

print("Thank you!")









    
