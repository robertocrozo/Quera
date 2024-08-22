def opface(num):
    op = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    if num in op:
        print(f"other way of {num} = {op[num]} .")
    else:
        print("invalid number")
num = int(input())
opface(num)
