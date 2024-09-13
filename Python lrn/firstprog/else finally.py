
f1 = open("#8timect.txt")

try:
    f = open("does2.txt")

except EOFError as e:
    print("Print eof error occured", e)

except IOError as e:
    print("Print IO error occured", e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")
