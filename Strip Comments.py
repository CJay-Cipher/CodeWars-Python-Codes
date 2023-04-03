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
# result == "apples, pears\ngrapes\nbananas"
"""

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


result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
print(result == "apples, pears\ngrapes\nbananas")

print(strip_comments(' a #b\nc\nd $e f g', ['#', '$']) == ' a\nc\nd')
print(strip_comments('a #b\nc\nd $e f g', ['#', '$']) == 'a\nc\nd')
print(strip_comments("\n", []) == "\n")