namespace: content

imports:
  op: content

flow:
  name: print-twice
  inputs:
    - text
  workflow:
    - print_once:
        do:
          op.print:
            - text
    
    - print_twice:
        do:
          op.print:
            -  text