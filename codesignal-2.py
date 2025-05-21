def solution(pattern: str, source: str) -> int:
    vowels = ["a", "e", "i", "o", "u", "y"]
    result = 0

    pattern_length = len(pattern)
    source_length = len(source)

    for i in range(source_length - pattern_length + 1):
        match = True
        for j in range(pattern_length):
            char = source[i + j]
            if (pattern[j] == '0' and char not in vowels) or (pattern[j] == '1' and char in vowels):
                match = False
                break
        if match:
            result += 1

    return result

print(solution("010", "amazing"))
print(solution("100", "codesignal"))
