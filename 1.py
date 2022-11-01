import re
s = input("Введите строку: ")
print(len(re.findall(r"=-\|", s)))
