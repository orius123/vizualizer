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
        navigate:
          SUCCESS1: print_twice
          FAILURE1: print_third
    
    - print_twice:
        do:
          op.print:
            -  text

    - print_third:
        do:
          op.print:
            -  text