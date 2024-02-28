a=int(input("請輸入數字a="))
b=int(input("請輸入數字b="))
c=int(input("請輸入數字c="))

answer=((-b)+(b**2 - 4*a*c)**(1/2))/(2*a)
answer1=((-b)-(b**2 - 4*a*c)**(1/2))/(2*a)
print("答案1是"+ str(answer))
print("答案2是"+ str(answer1))
