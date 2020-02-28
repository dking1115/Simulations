inp = input("sentence")
out=""
for i in inp:
    if(" " in i):
        out += " "
    else:
        out += "_"
print(out)