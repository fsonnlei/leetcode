def max_area(heights):
    left = 0
    right = len(heights) - 1
    current_max = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height

        current_max = max(area, current_max)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return current_max