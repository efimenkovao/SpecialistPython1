# Напишите программу, которая запрашивает строку до тех пор, пока пользователь не введет “хватит”.
# Т.е. программа запрашивает ввод, если вводится любое значение отличное от слова “хватит”,
# то программа запрашивает ввод снова.

# TODO: your code here
a = str(input("a: "))
while a != "хватит":
    print(a)
    a = str(input("a: "))
