from collections import defaultdict

def solution(numbers):
    counts = defaultdict(int)
    result = 0
    limit = 0
    constraint = pow(10,6)

    for i in range(100):
        if pow(2,i) // 2 > constraint: # constraint -10^6 <= numbers[i] <= 10^6
            limit = i
            break

    for first_element in numbers:
       counts[first_element] += 1

       for two_power in range(limit):
           second_element = pow(2, two_power) - first_element
           if second_element in counts:
                result += counts[second_element]
    return result

numbers = [1, -1, 2, 3]
print(solution(numbers))
numbers = [2]
print(solution(numbers))
numbers = [-2, -1, 0, 1, 2]
print(solution(numbers))