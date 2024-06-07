import queue
def markMissingParentheses(source:str):
    if len(source) == 0:
        return ""
    begin = 0
    mark_seq_right = ""
    stack = []
    char_list = []
    while begin < len(source):
        if source[begin] == ')':
            if len(stack) == 0:
                char_list.append("?")
            else:
                char_list[stack[-1]] = " "
                stack.pop(-1)
                char_list.append(" ")

        elif source[begin] == '(':
            # Search right to find a matching parentheses
            stack.append(begin)
            char_list.append("x")
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
