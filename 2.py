import re
s = input("Введите строку: ")
while re.search(r"\s[01]\d:[012345]\d:[012345]\d\s|\s2[0123]:[012345]\d:[012345]\d\s|\s[01]\d:[0-5]\d\s|\s2[0123]:[012345]\d\s", s):
    s = re.sub(r"[01]\d:[012345]\d:[012345]\d|2[0123]:[012345]\d:[012345]\d|[01]\d:[012345]\d|2[0123]:[012345]\d", "(TBD)", s, 1)
print(s)