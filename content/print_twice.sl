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
          SUCCESS: print_twice
          FAILURE: print_third
    
    - print_twice:
        do:
          op.print:
            -  text

    - print_third:
        do:
          op.print:
            -  text