class TuringMachineRomanSum:
    def __init__(self, tape):
        self.tape = list(tape)  # Convertimos la cinta en una lista para fácil manipulación
        self.head = 0           # Posición del cabezal de la máquina en la cinta
        self.states = {"INITIAL", "ADD", "SIMPLIFY", "HALT"}
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
            elif self.current_state == "ADD":
                self.state_add()
            elif self.current_state == "SIMPLIFY":
                self.state_simplify()
        
        # Al terminar, convertimos la cinta a un string de números romanos simplificados
        return "".join(self.tape).replace("#", "")
    
    # Estado Inicial: Convierte ambos números romanos en conjuntos de "I"
    def state_initial(self):
        new_tape = []
        for symbol in self.tape:
            if symbol != "#":
                new_tape.extend(self.expand_roman(symbol))
            else:
                new_tape.append("#")  # Añade el separador entre los dos números
        self.tape = new_tape
        self.current_state = "ADD"  # Cambia al siguiente estado para sumar
    
    # Estado de Adición: Combina todas las "I" de ambos números en una sola región
    def state_add(self):
        # Remueve el separador
        self.tape = [x for x in self.tape if x != "#"]
        self.current_state = "SIMPLIFY"
    
    # Estado de Simplificación: Convierte "I" en V, V en X, etc.
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
        while i_count >= 4:    # Manejo especial de IV
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
input_tape = "II#III"  # Representa "2 + 2"
turing_machine = TuringMachineRomanSum(input_tape)
result = turing_machine.run()
print("Resultado de la suma en números romanos:", result)
