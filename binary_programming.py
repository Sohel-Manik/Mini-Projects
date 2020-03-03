#Python 3.7.6
# Sahil Monish Lal

filename = input("Enter the new file name: ")
file = open("{}.txt".format(filename), 'w')
line_number = 0
while True:
    op = input("Opcode in Decimal: ")

    if op == "exit":
        file.close()
        break

    elif op.isalpha():
        print("Incorrect input")
    else:
        op = int(op)
        opcode = "{0:04b}".format(op)
        ope = int(input("Operand in Decimal: "))
        operand = "{0:012b}".format(ope)
        comment = input("Comment: ")

        file.write(f"{opcode}{operand} ; {line_number}: {op} {ope}  {comment}\n")
        line_number += 2
