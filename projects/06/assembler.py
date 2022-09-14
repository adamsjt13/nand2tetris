import parser
import code

def main(args):
    file_parser = parser.Parser(args)
    code_builder = code.Code()
    keep_going = True
    
    while keep_going:

        file_parser.advance()

        instruction = file_parser.instructionType()

        print('Instruction: ', instruction)
        if instruction == 'A_INSTRUCTION' or instruction == 'L_INSTRUCTION':
            print('Symbol: ', file_parser.symbol())
        else:
            print('Dest: ', file_parser.dest(), ' binary: ', code_builder.dest(file_parser.dest()))
            print('Comp: ', file_parser.comp(), ' binary: ', code_builder.comp(file_parser.comp()))
            print('Jump: ', file_parser.jump(), ' binary: ', code_builder.jump(file_parser.jump()))
        print('')
        keep_going = file_parser.hasMoreLines()

if __name__ == "__main__":
    import sys
    main(sys.argv[1])