def longest_run(L):
    d_count = 0
    i_count = 0
    max_count = 0
    index = 0

    for i in range(len(L) - 1):
        if L[i] <= L[i + 1]:
            i_count += 1
            if i_count > max_count:
                max_count = i_count
                index = i + 1
                print("i_count"+ str(i_count)+ " max_count" + str(max_count))
        else:
            i_count = 0
        if L[i] >= L[i + 1]:
            d_count += 1
            if d_count > max_count:
                max_count = d_count
                index = i + 1
        else:
            d_count = 0

    position = index - max_count
    return sum(L[position:index + 1 ])


L = [3, 3, 3, 3, 3, 3, 3, -10, 1, 2, 3, 4]
print(longest_run(L))