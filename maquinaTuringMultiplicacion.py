class TuringMachineRomanMultiplication:
    def __init__(self, tape):
        self.tape = list(tape)  # Convertimos la cinta en una lista para fácil manipulación
        self.head = 0           # Posición del cabezal de la máquina en la cinta
        self.states = {"INITIAL", "MULTIPLY", "SIMPLIFY", "HALT"}
        self.current_state = "INITIAL"
    
    # Función para convertir un símbolo romano en un conjunto de "I" en la cinta
    def expand_roman(self, symbol):
        mapping = {"I": "I", "V": "IIIII", "X": "IIIIIIIIII", 
                   "L": "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII",  # 50
                   "C": "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII",  # 100
                   "D": "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII",  # 500
                   "M": "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII"}  # 1000
        return list(mapping.get(symbol, ""))  # Devuelve la lista de "I"

    # Función principal que ejecuta la máquina de Turing
    def run(self):
        while self.current_state != "HALT":
            if self.current_state == "INITIAL":
                self.state_initial()
            elif self.current_state == "MULTIPLY":
                self.state_multiply()
            elif self.current_state == "SIMPLIFY":
                self.state_simplify()
        
        # Al terminar, convertimos la cinta a un string de números romanos simplificados
        return "".join(self.tape).replace("#", "")
    
    # Estado Inicial: Convierte ambos números romanos en conjuntos de "I"
    def state_initial(self):
        multiplicand = []
        multiplier = []
        before_separator = True  # Marca si estamos leyendo el multiplicando o el multiplicador

        # Convertimos los símbolos a "I" y separamos en multiplicando y multiplicador
        for symbol in self.tape:
            if symbol == "#":
                before_separator = False
                continue
            if before_separator:
                multiplicand.extend(self.expand_roman(symbol))
            else:
                multiplier.extend(self.expand_roman(symbol))

        self.tape = multiplicand + ["#"] + multiplier
        self.current_state = "MULTIPLY"
    
    # Estado de Multiplicación: Añade el multiplicando tantas veces como indica el multiplicador
    def state_multiply(self):
        multiplicand_count = self.tape[:self.tape.index("#")].count("I")
        multiplier_count = self.tape[self.tape.index("#") + 1:].count("I")
        
        # Calculamos el resultado como una cantidad total de "I"
        result_count = multiplicand_count * multiplier_count
        
        # Actualizamos la cinta con el resultado en forma de "I"
        self.tape = ["I"] * result_count
        self.current_state = "SIMPLIFY"
    
    # Estado de Simplificación: Convierte "I" en V, V en X, etc., para notación romana correcta
    def state_simplify(self):
        i_count = self.tape.count("I")
        self.tape = []  # Reiniciamos la cinta
        
        # Aplicamos las reglas de simplificación de menor a mayor
        while i_count >= 1000:
            self.tape.append("M")
            i_count -= 1000
        while i_count >= 500:
            self.tape.append("D")
            i_count -= 500
        while i_count >= 100:
            self.tape.append("C")
            i_count -= 100
        while i_count >= 50:
            self.tape.append("L")
            i_count -= 50
        while i_count >= 10:
            self.tape.append("X")
            i_count -= 10
        while i_count >= 5:
            self.tape.append("V")
            i_count -= 5
        while i_count >= 4:  # Manejo especial de IV
            if i_count == 4:
                self.tape.append("IV")
                i_count -= 4
            else:
                self.tape.append("V")
                i_count -= 5
        while i_count >= 1:
            self.tape.append("I")
            i_count -= 1

        self.current_state = "HALT"  # Termina el programa

# Ejemplo de uso
input_tape = "V#III"  # Representa "3 * 3"
turing_machine = TuringMachineRomanMultiplication(input_tape)
result = turing_machine.run()
print("Resultado de la multiplicación en números romanos:", result)
