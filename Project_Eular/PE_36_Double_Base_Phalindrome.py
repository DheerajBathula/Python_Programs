def baseconvert(n, base):
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    try:
        n = int(n)
        base = int(base)
    except:
        return ""

    if n < 0 or base < 2 or base > 36:
        return ""

    s = ""
    while 1:
        r = n % base
        s = digits[r] + s
        n = n / base
        if n == 0:
            break
    return s

def testPalindrome(string):
    for c in range(len(string)/2):
        if string[c] != string[-c-1]: return False
    return True
count = 0
n = map(int,raw_input().split())
for num in range(1,n[0]):
    dec_str = str(num)
    bin_str = baseconvert(num,n[1])
    if testPalindrome(dec_str) and testPalindrome(bin_str): count += num
print count
