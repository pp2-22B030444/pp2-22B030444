n=int(input())
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print('FizzBuzz', end = "")
    elif i%3==0:
        print('Fizz', end = "")
    elif i%5==0:
        print('Buzz', end = "")
    else:
        print(str(i), end="")


    if i==n:
        print('.',end=" ")
    else:
        print(',',end=" ")

    if i%10 ==0:
        print()

