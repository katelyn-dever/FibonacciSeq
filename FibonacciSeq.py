#FibonacciSeq.py
#Katelyn Dever
#Exercise 8.1

def Introduction():
    print("""The Fibonacci sequence starts 1,1,2,3,5,8...
    Each number in the sequence (after the first two) is the sum
    of the previous 2 numbers.  Your input will be used to find
    the nth number in the sequence""")

    userIndex = int(input("What is your number?: "))

    return userIndex

def FindNumber(n):
    #set up the list
    li = [1,1]
    count = 2

    while count <= n:
        #gets the length of the current list
        length = len(li)
        #finds the index of the last two numbers in the list
        index1 = length - 1
        index2 = length - 2
        #adds the two numbers in last two index locations together
        #stores as newNumber
        newNumber = li[index1] + li[index2]
        #appends the newNumber to the current list
        li.append(newNumber)
        #adds one to accumulator
        count = count +1
    return newNumber

def PrintResult(result):
    print("The result is", result)

def main():

    userIndex = Introduction()
    print(userIndex)
    result = FindNumber(userIndex)
    PrintResult(result)

main()
