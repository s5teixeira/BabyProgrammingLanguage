import lexer
import parserr
import evaluator
import decipher

print("\nHello baby language. \nEnter baby exp and see what you get. ")
while True:
    babyExp = input(">>> ")
    if babyExp == "poopoo":
        break
    srcCode = decipher.decipher(babyExp)
    print("Interpreted as: ", srcCode)
    tokSeq = lexer.tokenize(srcCode)
    rootNode = parserr.parse(tokSeq)
    result = evaluator.evaluate(rootNode)
    print("the result is: ", result)
print("now is time to go poopoo")