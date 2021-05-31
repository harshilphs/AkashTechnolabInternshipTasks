def sum(*no):
    sum = 0
    for i in no:
        sum += i
    return sum

result = sum(200,165)
print(result)

another_result = sum(145, 163, 200)
print(another_result)