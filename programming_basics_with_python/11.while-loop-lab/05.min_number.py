num = int(input())

num_list = []
while num:
    n = int(input())
    num_list.append(n)
    num -= 1
print(f"{min(num_list)}")
