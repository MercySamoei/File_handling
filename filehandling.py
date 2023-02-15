#This code opens a file.

project = open('try.txt','r')
print (project.read())

def is_palindrome(text):
    """
    A function that checks if a given string is a palindrome.
    """
    return text == text[::-1]

def find_palindrome(text):
    """
    A function that finds the first palindrome in a given string and returns it.
    """
    for i in range(len(text)):
        for j in range(i+1, len(text)):
            if is_palindrome(text[i:j]):
                return text[i:j]

    return None

# Testing the functions
text = "racecar is a palindrome"
palindrome = find_palindrome(text)

if palindrome:
    print("The palindrome is: ", palindrome)
else:
    print("No palindrome found in the text.")
