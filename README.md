Run main.py

# BabyProgrammingLanguage

# Description:
The BabyProgrammingLanguage is a Python project that parses mathematical expressions and executes programs written in simple custom baby language. The interpreter consists of three main components: the Lexer, the Parser, and the Evaluator. Together, these components allow users to input baby language code, which is then processed, evaluated, and executed, producing the desired output.

# Components:
-Lexer: Responsible for reading the source code of the BabyLang language and producing a sequence of tokens.  It scans the input text, recognizes individual elements and converts them into meaningful tokens. For example, it will tokenize the keywords "print," "number," and newline characters ("\n") as separate tokens.

-Parser: Takes the sequence of tokens produced by the Lexer and matches them to the language's grammar. It ensures that the tokens are arranged correctly and follow the defined syntax rules for the baby language.

-Evaluator: Knows the precedence of supported mathematical operations and applies an evaluation algorithm to solve expressions correctly. 

