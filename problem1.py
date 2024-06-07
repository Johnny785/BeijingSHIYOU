import queue
def countMinSubsequences(source:str, target:str):
    reverse_map = {}
    for i in range(len(source)):
        if not reverse_map.__contains__(source[i]):
            reverse_map[source[i]] = []
            reverse_map[source[i]].append(i)
        else:
            reverse_map[source[i]].append(i)
        
    current_index = -1
    subseq_count = 0
    step = 0
    while step < len(target):
        # No existence
        if not reverse_map.__contains__(target[step]):
            return -1
        # Find an index that is more than index
        found = False
        for index in reverse_map[target[step]]:
            if index > current_index:
                current_index = index
                found = True
                break
        if not found:
            subseq_count += 1
            current_index = -1
            continue
        step += 1

    # The last chunk will never be added since it will not detect an end of the current sequence, so we must account for that here
    return subseq_count + 1


if __name__ == "__main__":
    sourceList = ['abc', 'abc', 'xyz']
    targetList = ['abcbc', 'acdbc', 'xzyxz']
    resultList = [2, -1, 3]
    
    for i in range(3):
        try:
            result = countMinSubsequences(sourceList[i], targetList[i])
            assert result == resultList[i]
            print(f"Testcase number {i} passed")
        except:
            print(f"Test case number {i} failed, expected {resultList[i]}, received {result}")
