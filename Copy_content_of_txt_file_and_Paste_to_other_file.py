file1=input("Enter the name of First File : ")
file2=input("Enter the name of Second File : ")

# opening File 1 in read mode 
f1 = open(file1, 'r')

# opening File 2 in write mode
f2 = open(file2, 'w') 

# Reading the content from File 1 
content = f1.readlines() 

# Writing the Content in File 2 
for i in range(0, len(content)):
    f2.write(content[i]) 

# close the file 
f2.close() 
print("Content of first file has successfully copied to the second file ")

# open file 2 in read mode 
f2 = open(file2, 'r') 
  
# read the content of the file 
content1 = f2.read() 
  
# print the content of the file 
print("Content of Second file :")
print(content1) 
  
# close all files 
f1.close() 
f2.close()
