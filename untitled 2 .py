n = int(input("Number of jobs: "))
m = int(input("Number of machines: "))
pStr = input("Processing times: ")  # 3 3 3 4 4 5 5 6 7 8 

p = pStr.split(" ") #用空白分隔
for i in range(n):
  p[i] = int(p[i])
  list =[]
  list.append(p[i])
  print(list)
