def calc ():
    
    while True:

        n1 = float(input("Enter number 1: "))
        ope = input("Enter an operation (: ")
        n2 = float(input("Enter number 2: "))
    
        if ope == "+":
            result = n1 + n2
        elif ope == "-":
            result = n1 - n2
        elif ope == "*":
            result =  n1 * n2
        elif ope == "**":
            result =n1 ** n2
        elif ope == "/":
            if n2 == 0:
                result = "Error: 0 is not possible."
            else:
                result = n1 / n2
        print(result)
       

calc() 
    
