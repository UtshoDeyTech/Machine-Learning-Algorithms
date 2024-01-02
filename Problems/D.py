def kth_heaviest_box(k, weights):
    weights.sort(reverse=True)
    return weights[k - 1]


k = int(input())
weights = list(map(int, input().split()))

result = kth_heaviest_box(k, weights)
print(result)
