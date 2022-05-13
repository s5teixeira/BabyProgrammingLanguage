#EVALUTATOR >>>

def evaluate(rootNode):
    #base case
    if rootNode.lChild == None and rootNode.rChild == None:
        return int(rootNode.value)
    #recursive call
    else:
        result = 0
        leftResult = evaluate(rootNode.lChild)
        rightResult = evaluate(rootNode.rChild)
        if rootNode.type == "PLUS":
            result = leftResult + rightResult
        elif rootNode.type == "MINUS":
            result = leftResult - rightResult
        elif rootNode.type == "MULTIPLICATION":
            result = leftResult * rightResult
        elif rootNode.type == "DIVISION":
            result = leftResult / rightResult
        return result 