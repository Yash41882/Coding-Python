l=list(map(int,input("Enter numbers = ")))

print(l)
a=[0,0,7]
j=0
flag= False

for i in l:
    if(i == a[j]):
        j=j+1
        if(j==2):
            flag = True
            print("Code is found")
            break
    else:
        j=0
        
if(flag==False):
    print("Code not found")
