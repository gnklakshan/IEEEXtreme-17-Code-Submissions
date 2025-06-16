def largestrectangle(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area

def maximum_area(num_rectangles, min_height, heights):
    max_area = largestrectangle(heights)
    for i in range(num_rectangles):
        original_height = heights[i]
        if original_height < min_height:
            heights[i] = min_height
            max_area = max(max_area, largestrectangle(heights))
            heights[i] = original_height
    return max_area


num_rectangles, min_height = map(int, input().split())
heights = list(map(int, input().split()))


result = maximum_area(num_rectangles, min_height, heights)
print(result)
