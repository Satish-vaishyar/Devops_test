import sys
if (len(sys.argv) >= 3):
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
else:
    a = 10
    b = 30
    c = 16

a = int(a)
b = int(b)
c = int(c)

greatest = max(a, b, c)
print(f"Greatest Number: {greatest}") 