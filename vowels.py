# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word=input("Enter :")
vowels="AEIOU"
user_word=user_word.upper()
for letter in user_word:
    # Complete the body of the for loop.
    if letter in vowels:
        continue
    else:
        print(letter)

