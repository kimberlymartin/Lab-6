#25pt
total = 0
print "How many numbers would you like to add together?"
loops = int(raw_input())
for x in range(loops):
    print "Enter a number"
    number = raw_input()
    total = total + int(number)
print str(total) + " is your total"

#50pt
totalList = []
print "How many numbers would you like to add together?"
loops = int(raw_input())
for x in range(loops):
    print "Enter a number"
    number = int(raw_input())
    totalList.append(number)
print str(sum(totalList)) + " is your total"

#75pt
total = 1
print "What number would you like to find the factorial of?"
userInput = int(raw_input())
userRange = userInput + 1
for x in range(1,userRange,1):
    total = total * x
print "The answer is " + str(total)

#100pt
print "What numbers would you like to find the factors of?"
userInput = int(raw_input())
for x in range(1,userInput+1,1):
    if userInput % x == 0:
        print x