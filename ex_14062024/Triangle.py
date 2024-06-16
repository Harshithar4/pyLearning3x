s1 = int(input("Enter the length of first side in cms: "))
s2 = int(input("Enter the length of second side in cms: "))
s3 = int(input("Enter the length of third side in cms: "))
if s1 == s2 == s3:
    print("All sides are equal, It is a Triangle.")
elif s1 == s2 or s2==s3 or s1==s3:
    print("Two sides are equal,It is a isosceles.")
else:
    print("no sides are equal,It is a scalene.")
