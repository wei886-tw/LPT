# read and prepare n, m, and p

n = int(input("Number of jobs: "))
m = int(input("Number of machines: "))
pStr = input("Processing times: ")  # 3 3 3 4 4 5 5 6 7 8 

p = pStr.split(" ") #用空白分隔
for i in range(n):
  p[i] = int(p[i])

# machine completion times
loads = [0] * m   #為何要做這list
assignment = [0] * n

# in iteration j, assign job j to the least loaded machine
for j in range(n):           #?為什麼不是m+1

  # find the least loaded machine
  leastLoadedMachine = 0     #假設最少工作量的機器不知道是誰
  leastLoad = loads[0]       #假設這台機器工作量為第一個工作，list的[0]是第一個
  for i in range(1, m):      #?為什麼不是m+1
    if loads[i] < leastLoad: #如果loads[i]小於第一個工作量最小將i寫入最小load
      leastLoadedMachine = i 
      leastLoad = loads[i]

  # schedule a job
  loads[leastLoadedMachine] += p[j]
  assignment[j] = leastLoadedMachine + 1 #+1是為了呈現真實數字。List從0開始算起

  # the result
print("Job assignment: " + str(assignment))
print("Machine loads: " + str(loads))

