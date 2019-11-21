# 5 3
# 1 2 3 1 2
# 12, 3, 12, 123, 231, 312, 12312

'''
1 | 5
2 | 4
3 | 3
4 | 2
5 | 1

1 2 3 4 5
15 - 1 = 14

'''
n,m = map(int, input("n,m: ").split(" "))
A = list(map(int,input().split()))
# print('n:', n , ' m:',m , 'list:',A)

sum = 0

mod = [0 for i in range(m)]
mod[0] = 1
ans = 0
for i in range(n):
    sum += A[i]
    sum = sum % m

    mod[sum] += 1
    # print(sum)

ans = 0
for i in range(0,m):
    ans += mod[i] * (mod[i]-1) // 2
    # print(ans)

print(ans)
# print('mod: ',mod)