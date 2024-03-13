import re
my_text = input("Enter a String for Tokenization: ")
print("Tokenization of given input: ")
pattern = re.compile("ko+")
matches = pattern.finditer(my_text)
for token in matches:
    print(token)
