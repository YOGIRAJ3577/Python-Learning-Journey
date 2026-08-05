print("******************** Odd number between 1 and 20 ************************************")
for i in range(1,20):
    if i % 2 !=0:
        print(i)

print("******************** Table of 57 ************************************")
#Table of 57
for i in range (1, 11):
    print(57*i)

print("********************* multiple of 3 without 15***********************************")

for i in range (1,51):
    if i == 15:
        continue
    if i%3 == 0:
        print(i)

print("********************* multiple of 3 without 15***********************************")

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
for i in range (1, 1001):
    if(i%num1 ==0 and i%num2 ==0):
        print(i)
        break
