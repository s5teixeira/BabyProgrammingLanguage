# plusTreeNode = treeNode(plusTok.type, plusTok.value, getPrecedence(plusTok.type))


def getPrecedence(type):
    precedence = 0
    if type == "PLUS" or type == "MINUS":
        precedence = 1
    if type == "MULTIPLICATION" or type == "DIVISION":
        precedence = 2
    if type == "LPAREN" or type == "RPAREN":
        precedence = 3
    return precedence

def createTreeNodeList(tokSeq):
    dummyToken = Token("DUMMY", "")
    tokSeq.insert(0, dummyToken)
    tokSeq.append(dummyToken)
    treeNodeList = []
    s = 0  # adding variable to dec/inc
    for i in range(len(tokSeq)):
        token = tokSeq[i]
        lastToken = tokSeq[i - 1]
        newNode = treeNode(token.type, token.value, s + getPrecedence(token.type))
        if token.type == "LPAREN":
            s += 4
        elif token.type == "RPAREN":
            s -= 4
        elif token.type == "DUMMY":
            pass
        elif lastToken.type != "NUMBER" and token.type == "MINUS":  # parsing negative sign
            treeNodeList.append(treeNode("NUMBER", "0", 5 + s + getPrecedence("NUMBER")))
            treeNodeList.append(treeNode("MINUS", "-", 5 + s + getPrecedence("MINUS")))
            treeNodeList.append(treeNode("NUMBER", "1", 5 + s + getPrecedence("NUMBER")))
            treeNodeList.append(treeNode("MULTIPLICATION", "*", 4 + s + getPrecedence("MULTIPLICATION")))
        else:
            # adding new node
            treeNodeList.append(newNode)
    return treeNodeList

def parse(tokSeq):
    treeNodeList = createTreeNodeList(tokSeq)
    parsing(treeNodeList)
    if len(treeNodeList) == 3:
        treeNodeList[1].parent = None
    rootNode = findRoot(treeNodeList)
    return rootNode

def findRoot(treeNodelist):
    rootNode = None
    for node in treeNodelist:
        if node.parent == None and node.type != "DUMMY":
            rootNode = node
            break
    return rootNode

def printTree(rootNode):
    if rootNode.lChild == None and rootNode.rChild == None:
        # operand - leafs
        print(rootNode.value, end="")
    else:
        # operator - root & child
        print("(", end="")
        printTree(rootNode.lChild)
        print(rootNode.value, end="")
        printTree(rootNode.rChild)
        print(")", end="")

def parsing(treeNodeList):
    dummyNode = treeNode("DUMMY", "", 0)
    treeNodeList.insert(0, dummyNode)
    treeNodeList.append(dummyNode)
    # for each operand
    for index in range(len(treeNodeList)):
        node = treeNodeList[index]
        if node.type == "NUMBER":
            lOp = treeNodeList[index - 1]
            rOp = treeNodeList[index + 1]
            if rOp.precedence > lOp.precedence:
                # Right
                rOp.lChild = node
                node.parent = rOp
                if lOp.type != "DUMMY":
                    lOp.rChild = rOp
                    rOp.parent = lOp
            else:
                # Left
                lOp.rChild = node
                node.parent = lOp
                if rOp.type != "DUMMY":
                    # merge
                    while lOp.parent != None:
                        if lOp.parent.precedence < rOp.precedence:
                            break
                        lOp = lOp.parent
                    if lOp.parent != None:
                        lOp.parent.rChild = rOp
                        rOp.parent = lOp.parent
                    rOp.lChild = lOp
                    lOp.parent = rOp