input = input("How tall piramide is?(rows) ")
rows = int(input)
spaces = int(rows)
lines=1
smile_emoji="\U0001f600"
space = " "

while lines <= rows*2 :
    if lines%2 != 0 :
        print(space*spaces + smile_emoji*lines)
        spaces -= 1
    lines += 1