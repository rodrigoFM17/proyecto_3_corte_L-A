class TuringMachineRomanDivision:
    def __init__(self, tape):
        self.tape = list(tape)  # Convertimos la cinta en una lista para fácil manipulación
        self.head = 0           # Posición del cabezal de la máquina en la cinta
        self.states = {"INITIAL", "DIVIDE", "SIMPLIFY", "HALT"}
        self.current_state = "INITIAL"
    
    # Función para convertir un número romano en un conjunto de "I" en la cinta
    def expand_roman(self, roman):
        # Valores de cada símbolo romano
        mapping = {
            "I": 1, "V": 5, "X": 10, "L": 50, 
            "C": 100, "D": 500, "M": 1000
        }
        result = 0
        length = len(roman)
        
        # Convertir el número romano a su equivalente en "I" (valor entero)
        for i in range(length):
            if i + 1 < length and mapping[roman[i]] < mapping[roman[i + 1]]:
                result -= mapping[roman[i]]
            else:
                result += mapping[roman[i]]
        
        return ["I"] * result  # Expande el valor entero en "I"

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
        parts = ''.join(self.tape).split("#")
        dividend = self.expand_roman(parts[0])
        divisor = self.expand_roman(parts[1])

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
        self.current_state = "SIMPLIFY"
    
    # Estado de Simplificación: Convierte "I" en notación romana correcta
    def state_simplify(self):
        i_count = self.tape.count("I")
        self.tape = []  # Reiniciamos la cinta
        
        # Aplicamos las reglas de simplificación de menor a mayor
        while i_count >= 1000:
            self.tape.append("M")
            i_count -= 1000
        while i_count >= 900:
            self.tape.append("CM")
            i_count -= 900
        while i_count >= 500:
            self.tape.append("D")
            i_count -= 500
        while i_count >= 400:
            self.tape.append("CD")
            i_count -= 400
        while i_count >= 100:
            self.tape.append("C")
            i_count -= 100
        while i_count >= 90:
            self.tape.append("XC")
            i_count -= 90
        while i_count >= 50:
            self.tape.append("L")
            i_count -= 50
        while i_count >= 40:
            self.tape.append("XL")
            i_count -= 40
        while i_count >= 10:
            self.tape.append("X")
            i_count -= 10
        while i_count >= 9:
            self.tape.append("IX")
            i_count -= 9
        while i_count >= 5:
            self.tape.append("V")
            i_count -= 5
        while i_count >= 4:
            self.tape.append("IV")
            i_count -= 4
        while i_count >= 1:
            self.tape.append("I")
            i_count -= 1

        self.current_state = "HALT"  # Termina el programa

# Ejemplo de uso
input_tape = "XV#V"  # Representa "400 / 20"
turing_machine = TuringMachineRomanDivision(input_tape)
result = turing_machine.run()
print("Resultado de la división en números romanos:", result)
