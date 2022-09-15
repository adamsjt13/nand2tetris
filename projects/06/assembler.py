from parser import Parser
from code import Code

def main(args):

    parser = Parser(args)
    code = Code()

    output_file_name = args.replace('asm','hack')
    output_file = open(output_file_name, 'w')

    convert_to_binary = lambda x, n: format(int(x), 'b').zfill(n)

    print('file: ', output_file)
    while parser.hasMoreLines():

        parser.advance()

        if (parser.instructionType() == 'A_INSTRUCTION' 
            or parser.instructionType() == 'L_INSTRUCTION'):
            symbol = parser.symbol()
            symbol = convert_to_binary(symbol, 16)
            symbol = symbol + '\n'
            output_file.write(symbol)
        else:
            comp = code.comp(parser.comp())
            dest = code.dest(parser.dest())
            jump = code.jump(parser.jump())
            output = ''.join(['111',comp,dest,jump,'\n'])
            output_file.write(output)
    
    output_file.close()

if __name__ == "__main__":
    import sys
    main(sys.argv[1])