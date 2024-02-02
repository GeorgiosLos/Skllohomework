num = 100
sum = 0
i = 0
while i <= num:
    if i % 2 == 0:
        print(i)
        sum+=i
    i+=1
print(f"Sum of all the even numbers is {sum}")