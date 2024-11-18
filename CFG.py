class CalculatorParser:
    def __init__(self, input_string):
        self.input = input_string.replace(" ", "")  
        self.pos = 0  
    def parse(self):
       
        if self._E() and self.pos == len(self.input):
            return True  
        return False 

    def _E(self):
        
        if self._T():
            while self._current_char() and self._current_char() in "+-":  
                self._consume()  
                if not self._T():
                    return False
            return True
        return False

    def _T(self):
       
        if self._F():
            while self._current_char() and self._current_char() in "*/": 
                self._consume() 
                if not self._F():
                    return False
            return True
        return False

    def _F(self):
        
        char = self._current_char()
        if char == "(":
            self._consume() 
            if not self._E():
                return False
            if self._current_char() == ")":
                self._consume()  
                return True
            return False
        elif char and char.isdigit(): 
            return self._NUM()
        return False

    def _NUM(self):
        
        if self._current_char() and self._current_char().isdigit():
            while self._current_char() and self._current_char().isdigit():
                self._consume()  
            return True
        return False

    def _current_char(self):
        
        if self.pos < len(self.input):
            return self.input[self.pos]
        return None

    def _consume(self):
       
        if self.pos < len(self.input):  
            self.pos += 1


def validate_expression(expression):
    parser = CalculatorParser(expression)
    if parser.parse():
        return f"La expresión '{expression}' es válida."
    else:
        return f"La expresión '{expression}' no es válida."

