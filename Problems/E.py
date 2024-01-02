def scariest_halloween(n, costumes):
    costume_count = {}
    for costume in costumes:
        costume_count[costume] = costume_count.get(costume, 0) + 1
    
    scariest_subsequence = []
    max_occurrence = max(costume_count.values())

    if max_occurrence < 2:
        print(-1)
        return

    for costume in reversed(costumes):
        if costume_count[costume] == max_occurrence:
            scariest_subsequence.append(costume)

    print(" ".join(map(str, scariest_subsequence)))

n1 = int(input())
costumes1 = list(map(int, input().split()))
scariest_halloween(n1, costumes1)
