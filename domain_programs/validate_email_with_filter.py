# Enter your code here. Read input from STDIN. Print output to STDOUT
def validate(x):
    if not "@" in x or not "." in x:
        return False
    if x.index("@") > x.index("."):
        return False
    split_at = x.split("@")
    if len(split_at) != 2:
        return False
    user_name = split_at[0]
    if len(split_at[1].split(".")) !=2:
        return False
    website = split_at[1].split(".")[0]
    extension = split_at[1].split(".")[1]
    if not user_name or not website or not extension or len(extension) > 3 :
        return False
    else:
        for i in user_name:
            if ((not i.isalnum()) and (not str(i) == "_") and (not str(i) == "-")):
                return False
        for i in website:
            if ((not i.isalnum())):
                return False
        for i in extension:
            if not i.isalpha():
                return False
    return True
                
l = []
final_list = []
n = int(raw_input())
for i in range(n):
    l.append(raw_input())
for i in l:
    result = validate(i)
    if result:
        final_list.append(i)
print sorted(final_list, key=str.lower)
