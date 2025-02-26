def big(n):
    return max(map(int, str(n)))

num = int(input("Enter a number: "))
print("Big:", big(num))
