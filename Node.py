class Node:
    def __init__(self, value):
        self.value = value 
        self.children = []

    def __repr__(self):
        return f"Node({self.value}, children={self.children})"

    def evaluate(self):
        """Evalúa el valor de la expresión representada por el árbol."""
        if not self.children:  
            return float(self.value)  
        elif len(self.children) == 2:  
            left_value = self.children[0].evaluate()
            right_value = self.children[1].evaluate()
            if self.value == "+":
                return left_value + right_value
            elif self.value == "-":
                return left_value - right_value
            elif self.value == "*":
                return left_value * right_value
            elif self.value == "/":
                if right_value == 0:
                    raise ZeroDivisionError("No se puede dividir por cero.")
                return left_value / right_value
        raise ValueError("Nodo inválido en el árbol.")

class CalculatorParser:
    def __init__(self, input_string):
        self.input = input_string.replace(" ", "")  
        self.pos = 0  

    def parse(self):
        
        tree = self._E()
        if tree and self.pos == len(self.input):
            return tree  
        return None  

    def _E(self):
        
        left = self._T()
        if not left:
            return None
        while self._current_char() and self._current_char() in "+-":
            operator = self._current_char()
            self._consume() 
            right = self._T()
            if not right:
                return None
            node = Node(operator)
            node.children.append(left)
            node.children.append(right)
            left = node
        return left

    def _T(self):
        
        left = self._F()
        if not left:
            return None
        while self._current_char() and self._current_char() in "*/":
            operator = self._current_char()
            self._consume()  
            right = self._F()
            if not right:
                return None
            node = Node(operator)
            node.children.append(left)
            node.children.append(right)
            left = node
        return left

    def _F(self):
        
        char = self._current_char()
        if char == "(":
            self._consume()  
            subtree = self._E()
            if not subtree or self._current_char() != ")":
                return None
            self._consume() 
            return subtree
        elif char and char.isdigit():
            return self._NUM()
        return None

    def _NUM(self):
        
        start = self.pos
        while self._current_char() and self._current_char().isdigit():
            self._consume() 
        return Node(self.input[start:self.pos]) 
    def _current_char(self):
        
        if self.pos < len(self.input):
            return self.input[self.pos]
        return None

    def _consume(self):
        
        if self.pos < len(self.input):  
            self.pos += 1
