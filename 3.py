import re
s = input("Введите строку: ")
if re.fullmatch(r"[\w\.]+@[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+|[\w\.]+@[a-zA-Z]+\.[a-zA-Z]+", s):
    print(re.search(r"@.+",s)[0][1:])
else:
    print("Fail!")