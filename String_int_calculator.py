#Python Program to get the last integer from string and print its sum and average. Program will stop when input is 0.

number=[] #declaring a list to store the integer values
string='intialization' #initializing the string variable with random value
count=-1 #intializing the count variable to count the number of input excluding 0

# Taking String input fron the user
while(string!='0'):
    count+=1
    string = str(input())
    res=(string[-1])
    #print(res)
    if (res.isnumeric()):
        res=int(res)
        number.append(res)
    
#Calculating the total sum of the integers    
length = len(number) - 1 # excluding 0 as it is not needed to be added
total = 0 #intializing the total variable
for j in range(0, length):
    total = total + number[j]

# Calculating the average of the integer 
average = (total / count)
    
print("Number of User inputs = ",count)
print("Total of These Integers = ",total)
print("Average of the Integers = ", format(average,".1f"))
