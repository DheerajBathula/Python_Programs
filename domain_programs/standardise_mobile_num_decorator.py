n = int(raw_input())
nums = []
final = []
for i in range(n):
    nums.append(raw_input())
for num in sorted(nums,key=int):
    last5 = num[-5:]
    first5 = num[:-5][-5:]
    x = "+91 "+str(first5).strip()+" "+str(last5).strip()
    final.append(x)
for i in sorted(final):
    print i
