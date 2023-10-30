#unlimited size stack
class UnlimitedStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
#---------------------------------------
#Implement limited size stack
class limitedSizeStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, item):
        if len(self.stack) < self.max_size:
            self.stack.append(item)
        else:
            print("stack is full. cannot push item:", item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("stack is empty cannot pop")
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty cannot peek")
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
#-----------------------------------------------------
#Reverse the content of file using Stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def reverse_content(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            content = f.read()

        stack = Stack()
        for char in content:
            stack.push(char)

        reversed_content = ""
        while not stack.is_empty():
            reversed_content += stack.pop()

        with open(output_file, 'w') as f:
            f.write(reversed_content)

        print("Content reversed and saved to", output_file)

    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output.txt"
    reverse_content(input_filename, output_filename)

#------------------------------------------------------------------
#match the parenthesis using stack
def match_parentheses(expression):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_map = {")": "(", "}": "{", "]": "["}
    
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    
    return len(stack) == 0
#-----------------------------------------------------------------
#Match the tags in HTML file using Stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

def match_html_tags(html):
    stack = Stack()
    i = 0

    while i < len(html):
        if html[i] == '<':
            if i + 1 < len(html) and html[i + 1] == '/':
                i += 2
                tag_name = ""
                while i < len(html) and html[i] != '>':
                    tag_name += html[i]
                    i += 1
                if stack.is_empty() or stack.pop() != tag_name:
                    return False
            else:
                i += 1
                tag_name = ""
                while i < len(html) and html[i] != '>':
                    tag_name += html[i]
                    i += 1
                stack.push(tag_name)
        else:
            i += 1

    return stack.is_empty()
#------------------------------------------------------
#signature stack transfer
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())
#-------------------------------------------
#browser navigation
class BrowserNavigation:
    def __init__(self):
        self.backward_stack = []
        self.forward_stack = []

    def navigate(self, url):
        self.backward_stack.append(url)
        self.forward_stack = []

    def go_back(self):
        if self.backward_stack:
            current_url = self.backward_stack.pop()
            self.forward_stack.append(current_url)
            return current_url
        else:
            print("No more pages to go back to.")
            return None

    def go_forward(self):
        if self.forward_stack:
            current_url = self.forward_stack.pop()
            self.backward_stack.append(current_url)
            return current_url
        else:
            print("No more pages to go forward to.")
            return None
#--------------------------------------------------------------
#Modify Q5 such that HTML tags may contain attributes along with tag name
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

def match_html_tags(html):
    stack = Stack()
    i = 0

    while i < len(html):
        if html[i] == '<':
            i += 1
            tag = ""
            while i < len(html) and html[i] != '>' and not html[i].isspace():
                tag += html[i]
                i += 1
            if tag.startswith('/'):
                if stack.is_empty() or stack.pop() != tag[1:]:
                    return False
            else:
                stack.push(tag)
        else:
            i += 1

    return stack.is_empty()
#--------------------------------------------