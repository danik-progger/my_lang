# my-lang

## This project is a code from MIPT course on programming languages theory
#### It contains code that creates minimal full determined automaton from regular expressions, scanner and own interpreted language made with use of antlr4

1. In folders regex and automatons you can find code that creates minimal full determined automaton from regular expressions, scanner and own interpreted language made with use of antlr4

    It uses algorithm that converts regular expression to naive non-determined automaton with epsilon transitions. Then it gets rid of epsilon transitions. Next iteration is determining automatons. The last two steps are making it minimal and then making it full by adding "trash" state

2. In folder scanner you can find code for scanner. It reads the string and recognizes the type of each part of code string

3. In folder interpreter you can find code for own language made with antlr4

### Use and tests

1. To see how algorithm of making minimal full determined finite automaton works you can uncomment line 66: "# test_minimal_dfa_from_regex()" and run file test.py

2. To test how scanner works you can just run file test.py
   
3. To see how my own language works you can see code in input.lang and run it with command "python Driver.pt input.lang" to see what tis code does and find the syntactic parsing tree in tree.out
