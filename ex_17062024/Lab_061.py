# def say_hello():
#     print("Hello")
#
# say_hello()

def say_hello(name="Bharath"):
    print("Hello", name)


say_hello()
say_hello("Ganishka")
say_hello(name="puttu")


def sum_number(a, b):
    return (a + b)


result = sum_number(3, 8)
print(result)
result = sum_number(a=5, b=9)
print(result)
result = sum_number(2, b=9)
print(result)
