sentence = input("Enter a sentence: ")

chars = len(sentence)
print("Number of characters:", chars)

words = len(sentence.split())
print("Number of words:", words)

vowels = 0
spaces = 0
digits = 0

for ch in sentence:
    if ch in "aeiouAEIOU":
        vowels = vowels + 1
    if ch == " ":
        spaces = spaces + 1
    if ch >= "0" and ch <= "9":
        digits = digits + 1

print("Number of vowels:", vowels)
print("Number of spaces:", spaces)
print("Number of digits:", digits)
