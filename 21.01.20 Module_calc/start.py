from lib.calc import plus, minus, mult, dev

print("Hello! Choose an action! \n Enter 1,2,3,4 or 5")
print("1 - +")
print("2 - -")
print("3 - *")
print("4 - /")
print("5. Quit \n")

action = int(input("Enter action: "))
if action == 1:
    res = plus(2, 3, 10)
    print("sum =", res, "\n")
elif action == 2:
    res = minus(2, 3, 10)
    print("Subtraction =", res, "\n")
elif action == 3:
    mult = res(2, 3, 10)
    print("Multiplication =", res, "\n")
elif action == 4:
    dev = res(2, 3, 10)
    # print("Division =", res, "\n")


 



