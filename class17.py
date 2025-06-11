'''Break
Outline:
Write a program to check alphabet “A” is present in the given string or not. 
And terminate the loop after finding the alphabet “A.”
string = "program"#input("Enter a string: ")
for i in string:
    if i == "a":
        #print("A has been found",end=":")
        #print("a")
        break
    #else:
    #    print("A is not found",end=":")
    print(i)'''

'''Pass
Outline:
Write a program to satisfy the following conditions of the given range: If the number is divisible by 20, 
it provides an output "twist." If the number is divisible by 15, it will pass (no output) If the number is
divisible by 5, it will give an output “fizz.” If the number is divisible by 3, it will give an output "buzz."
Otherwise, it will give the output of that number.
n = int(input("Enter a number n: "))
if n%20 == 0 and n%15 !=0:
    print("twist")
if n%15 == 0:
    pass
if n%5 == 0 and n%15 !=0:
    print("fizz")
if n%3 == 0 and n%15 !=0:
    print("buzz")'''

'''Continue
Outline:
Write a program to display 1 to 10 numbers in reverse order and skip the number 5.
for i in range(10,0,-1):
    if i == 5:
        continue
    print(i)'''

'''
def add(a, b):
    return a+b
n = add(19, 1)
print(n)
'''
