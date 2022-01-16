import random

def ArrayChallenge(num):
    l = [int(i) for i in str(num)]
    count = 1
    l2 = []
    random_num = random.choice(l)
    print("l = ", l)
    print("Random int from l = ",random_num)
    for i in range(len(l)):
        new = random_num * l[i]
        l.append(new)
        l2.append(new)
    print("l2 = ", l2)
    while(True):
        print("list = ", l)
        for i in range(len(l)):
            if i+1 < len(l) and (l[i] == l[i+1]):
                print("Equal Elements : ", l[i]," , ", l[i+1])
                return count
        
        random_num2 = random.choice(l2)
        print("Random int from l2 = ",random_num2)
        count += 1
        for i in range(len(l2)):
            new2 = random_num2 * l[i]
            l.append(new2)
            l2[i] = new2


num = int(input("Enter a number = "))
print(ArrayChallenge(num))
