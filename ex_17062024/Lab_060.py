def f1(a=3, b=4, c=5):
    print("This code will work")  # If we write print after return it will not work inside function
    return (a + b + c)


print("End")

result1 = f1(2, 3, 4)
print(result1)
result2 = f1(1)
print(result2)
result3 = f1(2, 2)
print(result3)
