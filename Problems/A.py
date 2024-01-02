def max_chocolates(n, s, chocolates):
    chocolates.sort()
    total_sugar = 0
    count = 0

    for sugar in chocolates:
        if total_sugar + sugar <= s:
            total_sugar += sugar
            count += 1
        else:
            break

    return count


n = int(input())
s = int(input())
chocolates = list(map(int, input().split()))


result = max_chocolates(n, s, chocolates)
print(result)
