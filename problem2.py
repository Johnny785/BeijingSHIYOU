import queue
def markMissingParentheses(source:str):
    if len(source) == 0:
        return ""
    begin = 0
    stack = []
    char_list = [] # Stores characters of the current mark string
    # Push begin to the right
    while begin < len(source):
        # Try to match right parentheses to left parentheses, otherwise mark as ?
        if source[begin] == ')':
            if len(stack) == 0:
                char_list.append("?")
            else:
                char_list[stack[-1]] = " "
                stack.pop(-1)
                char_list.append(" ")
        # Add index to the stack if we encounter left parentheses, and default mark to x
        elif source[begin] == '(':
            stack.append(begin)
            char_list.append("x")
        # Add space for all other characters
        else:
            char_list.append(" ")
        begin += 1


    return (source + "\n" + "".join(char_list)).rstrip()
        


if __name__ == "__main__":
    sourceList = ['bge)))))))))', '((IIII))))))', '()()()()(uuu', '))))UUUU((()']
    resultList = ['bge)))))))))\n   ?????????', '((IIII))))))\n        ????', '()()()()(uuu\n        x', '))))UUUU((()\n???? xx']
    
    for i in range(3):
        result = markMissingParentheses(sourceList[i])
        try:
            assert result == resultList[i]
            print(f"Testcase number {i} passed")
        except:
            print(f"Test case number {i} failed")

        print("Expected sequence is: \n" + resultList[i])
        print("Received sequence is: \n" + result)
