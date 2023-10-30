from stack import *


#-----------------------------
#unlimited stack test
stack = UnlimitedStack()

stack.push(10)
stack.push(20)
assert stack.peek() == 20

popped_item = stack.pop()
assert popped_item == 20
assert stack.peek() == 10

assert not stack.is_empty()
assert stack.size() == 1

stack.pop()
assert stack.is_empty()
assert stack.size() == 0

print("all tests passed!")
#------------------------------
stack = limitedSizeStack(max_size = 3)

stack.push(10)
stack.push(20)
stack.push(30)
assert stack.peek() == 30

stack.push(40)

popped_item = stack.pop()
assert popped_item == 30
assert stack.peek() == 20

assert not stack.is_empty()
assert stack.size() == 2

stack.pop()
stack.pop()
assert stack.is_empty()
assert stack.size() == 0

print("All tests passed!")

#------------------------------------------
# Match the parentheses using Stack
def test_matching():
    assert match_parentheses("((()))") == True
    assert match_parentheses("{[()]}") == True
    assert match_parentheses("{[(])}") == False
    assert match_parentheses("[{()}]") == True
    assert match_parentheses("((())") == False
    assert match_parentheses("())(") == False

if __name__ == "__main__":
    test_matching()
    print("All tests passed in parenthesis.")
#-----------------------------------------------
#
html_content = """
<html>
<head>
<title>Matching HTML Tags</title>
</head>
<body>
<div>
<p>This is a test</p>
</div>
</body>
</html>
"""

if match_html_tags(html_content):
    print("HTML tags are properly matched.")
else:
    print("HTML tags are not properly matched.")

#-----------------------------------------------------
#signature stack transfer
S = Stack()
T = Stack()

elements_to_transfer = [1, 2, 3, 4, 5]
for element in elements_to_transfer:
    S.push(element)

transfer(S, T)

expected_result = list(reversed(elements_to_transfer))
actual_result = []
while not T.is_empty():
    actual_result.append(T.pop())

assert expected_result == actual_result[::-1], "Transfer function did not work as expected."

print("Transfer test passed.")
#---------------------------------------------------------------------
#browser navigation
browser = BrowserNavigation()

# Navigate to URLs
browser.navigate("https://www.example.com")
browser.navigate("https://www.openai.com")
browser.navigate("https://www.google.com")

# Test go_back()
assert browser.go_back() == "https://www.openai.com"
assert browser.go_back() == "https://www.example.com"
assert browser.go_back() is None

# Test go_forward()
assert browser.go_forward() == "https://www.example.com"
assert browser.go_forward() == "https://www.openai.com"
assert browser.go_forward() == "https://www.google.com"
assert browser.go_forward() is None

print("Browser navigation test passed.")
#------------------------------------------------------
#Modify Q5 such that HTML tags may contain attributes along with tag name
valid_html = "<div id='myDiv'><p>Some text</p></div>"
invalid_html = "<div><p>Unclosed tag</div>"
valid_nested_html = "<div><p>Some text <span>with nested</span> elements</p></div>"

assert match_html_tags(valid_html) is True, "Valid HTML tags not recognized."
assert match_html_tags(invalid_html) is False, "Invalid HTML tags not detected."
assert match_html_tags(valid_nested_html) is True, "Valid nested HTML tags not recognized."

print("HTML tag matching tests passed.")
#---------------------------------------------------------