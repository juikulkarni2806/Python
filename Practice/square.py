#Accept two values S and N. Print square of first N numbers starting from S.
print("Please Enter Two Numbers")
S=int(input("Enter First Number: "))
N=int(input("Enter Your Limit: "))
for i in range (S,N+S):
    print(i*i)
    