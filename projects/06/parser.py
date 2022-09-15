class Parser:
    def __init__(self, file_name):
        file = open(file_name, 'r')
        self._lines = file.readlines()
        self._current_line_number = -1
        self._current_line = ''

    def hasMoreLines(self):
        return self._current_line_number < len(self._lines) - 1

    def cleanLine(self):
        self._current_line = self._lines[self._current_line_number].replace('\n','')
        self._current_line = self._current_line.replace(' ','')
        comment_index = self._current_line.find('//')
        if comment_index > 0:
            self._current_line = self._current_line[0:comment_index]
        elif comment_index == 0:
            self._current_line = ''

    def isBlankLine(self):
        return len(self._current_line) == 0

    def isComment(self):
        if not(self.isBlankLine()):
            return self._current_line[0] == "/"
    
    def advance(self):
        self._current_line_number += 1
        self.cleanLine()
        if self.isBlankLine():
            self.advance()
        
    
    def instructionType(self):
        if self._current_line[0] == '@':
            return 'A_INSTRUCTION'
        elif '=' in self._current_line or ';' in self._current_line:
            return 'C_INSTRUCTION'
        elif '(' and ')' in self._current_line:
            return 'L_INSTRUCTION'
        
    def symbol(self):
        self._current_line = self._current_line.replace('@','')
        self._current_line = self._current_line.replace('(','')
        self._current_line = self._current_line.replace(')','')

        return self._current_line

    def dest(self):
        equal_index = self._current_line.find('=')
        if equal_index != -1:
            return self._current_line[0:equal_index]
    
    def comp(self):
        equal_index = self._current_line.find('=')
        colon_index = self._current_line.find(';')

        if colon_index != -1:
            return self._current_line[(equal_index+1):colon_index]
        else:
            return self._current_line[(equal_index+1):len(self._current_line)]

    def jump(self):
        colon_index = self._current_line.find(';')

        if colon_index != -1:
            return self._current_line[(colon_index)+1:len(self._current_line)]

