number=int(input("Enter the number: "))
n1=0
n2=1
if number<=0:
    print("Enter a positive number")
else:
    print("Fibonacci series:")
    for i in range(number):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
       