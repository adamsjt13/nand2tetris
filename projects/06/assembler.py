from parser import Parser
from code import Code
from symbol_table import SymbolTable

def main(args):

    parser = Parser(args)
    code = Code()
    symbol_table = SymbolTable()

    output_file_name = args.replace('asm','hack')
    output_file = open(output_file_name, 'w')

    convert_to_binary = lambda x, n: format(int(x), 'b').zfill(n)

    line_number = 0

    print('file: ', output_file)
    ######## First Pass ########
    while parser.hasMoreLines():

        parser.advance()

        if (parser.instructionType() == 'A_INSTRUCTION' 
            or parser.instructionType() == 'C_INSTRUCTION'):
            line_number += 1
        elif parser.instructionType() == 'L_INSTRUCTION':
            symbol = parser.symbol()
            if not(symbol_table.contains(symbol)):
                symbol_table.addEntry(symbol, line_number)

    ######## Second Pass ########
    parser = Parser(args)
    current_ram_address = 16

    while parser.hasMoreLines():

        parser.advance()
        
        if parser.instructionType() == 'A_INSTRUCTION':
            symbol = parser.symbol()
            try: 
                output = convert_to_binary(int(symbol), 16) + '\n'  
                output_file.write(output)

            except ValueError:
                if not(symbol_table.contains(symbol)):
                    symbol_table.addEntry(symbol, current_ram_address)
                    current_ram_address += 1
                symbol_address = symbol_table.getAddress(symbol)
                output = convert_to_binary(symbol_address, 16) + '\n'
                output_file.write(output)

        elif parser.instructionType() == 'C_INSTRUCTION':
            comp = code.comp(parser.comp())
            dest = code.dest(parser.dest())
            jump = code.jump(parser.jump())
            output = ''.join(['111',comp,dest,jump,'\n'])
            output_file.write(output)
  
    output_file.close()

if __name__ == "__main__":
    import sys
    main(sys.argv[1])