"""
Complete the solution so that it strips all text that follows any of a set of comment
markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""

# My code
def strip_comments(input_str, markers):
    input_str = input_str.split("\n")
    for x in range(len(input_str)):
        var = ""
        for y in input_str[x]:
            if y in markers:
                break
            var += y
        input_str[x] = var.rstrip()
    return "\n".join(input_str)


ans = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
print(ans == "apples, pears\ngrapes\nbananas")

# ChatGPT code
def solution1(input_str, markers):
    lines = input_str.split('\n')  # split input string into lines
    for i in range(len(lines)):
        for marker in markers:
            if marker in lines[i]:
                lines[i] = lines[i].split(marker)[0].rstrip()  # strip text after the marker and whitespace at the end
    return '\n'.join(lines)  # join lines back together with newline characters


print(solution1(' a #b\nc\nd $e f g', ['#', '$']) == ' a\nc\nd')

# Trust code
def solution2(sentence: str, markers: list):
    sentence = sentence.splitlines()
    for i in range(len(sentence)):
        for marker in markers:
            ind = sentence[i].find(marker)
            if ind != -1:
                sentence[i] = sentence[i][:ind].rstrip()

    return "\n".join(sentence)


print(solution2(' a #b\nc\nd $e f g', ['#', '$']) == ' a\nc\nd')

# solution('a #b\nc\nd $e f g', ['#', '$']) == 'a\nc\nd'
# solution("\n", []) == "\n"