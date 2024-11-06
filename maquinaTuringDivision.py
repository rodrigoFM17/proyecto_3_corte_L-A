class TuringMachineRomanDivision:
    def __init__(self, tape):
        self.tape = list(tape)  # Convertimos la cinta en una lista para fácil manipulación
        self.head = 0           # Posición del cabezal de la máquina en la cinta
        self.states = {"INITIAL", "DIVIDE", "SIMPLIFY", "HALT"}
        self.current_state = "INITIAL"
    
    # Función para convertir un símbolo romano en un conjunto de "I" en la cinta
    def expand_roman(self, symbol):
        mapping = {
            "I": "I", 
            "V": "I" * 5, 
            "X": "I" * 10, 
            "L": "I" * 50,  
            "C": "I" * 100,  
            "D": "I" * 500,  
            "M": "I" * 1000  
        }
        return list(mapping.get(symbol, ""))  # Devuelve la lista de "I"

    # Función principal que ejecuta la máquina de Turing
    def run(self):
        while self.current_state != "HALT":
            if self.current_state == "INITIAL":
                self.state_initial()
            elif self.current_state == "DIVIDE":
                self.state_divide()
            elif self.current_state == "SIMPLIFY":
                self.state_simplify()
        
        # Al terminar, convertimos la cinta a un string de números romanos simplificados
        return "".join(self.tape).replace("#", "")
    
    # Estado Inicial: Convierte ambos números romanos en conjuntos de "I"
    def state_initial(self):
        dividend = []
        divisor = []
        before_separator = True  # Marca si estamos leyendo el dividendo o el divisor

        # Convertimos los símbolos a "I" y separamos en dividendo y divisor
        for symbol in self.tape:
            if symbol == "#":
                before_separator = False
                continue
            if before_separator:
                dividend.extend(self.expand_roman(symbol))
            else:
                divisor.extend(self.expand_roman(symbol))

        self.tape = dividend + ["#"] + divisor
        self.current_state = "DIVIDE"
    
    # Estado de División: Sustrae el divisor del dividendo sucesivamente y cuenta las veces
    def state_divide(self):
        dividend_count = self.tape[:self.tape.index("#")].count("I")
        divisor_count = self.tape[self.tape.index("#") + 1:].count("I")
        
        # Si el divisor es 0 (inexistente), división no se puede realizar
        if divisor_count == 0:
            print("Error: División entre cero.")
            self.current_state = "HALT"
            return
        
        # Calculamos el cociente como la cantidad de veces que el divisor cabe en el dividendo
        quotient_count = 0
        while dividend_count >= divisor_count:
            dividend_count -= divisor_count
            quotient_count += 1
        
        # Actualizamos la cinta con el cociente en forma de "I"
        self.tape = ["I"] * quotient_count
        print("Cociente en 'I' antes de simplificar:", ''.join(self.tape))  # Depuración
        self.current_state = "SIMPLIFY"
    
    # Estado de Simplificación: Convierte "I" en V, V en X, etc., para notación romana correcta
    def state_simplify(self):
        i_count = self.tape.count("I")
        self.tape = []  # Reiniciamos la cinta
        
        # Aplicamos las reglas de simplificación de menor a mayor
        while i_count >= 1000:
            self.tape.append("M")
            i_count -= 1000
        while i_count >= 900:  # Manejo especial de CM
            self.tape.append("CM")
            i_count -= 900
        while i_count >= 500:
            self.tape.append("D")
            i_count -= 500
        while i_count >= 400:  # Manejo especial de CD
            self.tape.append("CD")
            i_count -= 400
        while i_count >= 100:
            self.tape.append("C")
            i_count -= 100
        while i_count >= 90:  # Manejo especial de XC
            self.tape.append("XC")
            i_count -= 90
        while i_count >= 50:
            self.tape.append("L")
            i_count -= 50
        while i_count >= 40:  # Manejo especial de XL
            self.tape.append("XL")
            i_count -= 40
        while i_count >= 10:
            self.tape.append("X")
            i_count -= 10
        while i_count >= 9:  # Manejo especial de IX
            self.tape.append("IX")
            i_count -= 9
        while i_count >= 5:
            self.tape.append("V")
            i_count -= 5
        while i_count >= 4:  # Manejo especial de IV
            self.tape.append("IV")
            i_count -= 4
        while i_count >= 1:
            self.tape.append("I")
            i_count -= 1

        print("Resultado simplificado:", ''.join(self.tape))  # Depuración final
        self.current_state = "HALT"  # Termina el programa

# Ejemplo de uso
input_tape = "CD#XX"  # Representa "400 / 20"
turing_machine = TuringMachineRomanDivision(input_tape)
result = turing_machine.run()
print("Resultado de la división en números romanos:", result)
