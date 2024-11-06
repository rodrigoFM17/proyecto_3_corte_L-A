class TuringMachineRomanSubtraction:
    def __init__(self, tape):
        self.tape = tape  # Mantiene la cinta como una cadena
        self.current_state = "INITIAL"
    
    # Mapeo de valores romanos a enteros
    roman_to_int_map = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    
    # Mapeo inverso de enteros a números romanos para la simplificación final
    int_to_roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    # Convierte un número romano a un entero
    def roman_to_int(self, roman):
        total = 0
        prev_value = 0
        for symbol in reversed(roman):
            value = self.roman_to_int_map[symbol]
            if value < prev_value:
                total -= value  # Resta si el símbolo actual es menor que el anterior
            else:
                total += value
            prev_value = value
        return total
    
    # Convierte un entero a notación romana simplificada
    def int_to_roman(self, number):
        result = []
        for (value, symbol) in self.int_to_roman_map:
            while number >= value:
                result.append(symbol)
                number -= value
        return "".join(result)
    
    # Función principal que ejecuta la máquina de Turing
    def run(self):
        if self.current_state == "INITIAL":
            # Divide los dos números romanos en la cinta
            minuend_roman, subtrahend_roman = self.tape.split("#")
            minuend = self.roman_to_int(minuend_roman)
            subtrahend = self.roman_to_int(subtrahend_roman)
            
            # Realiza la resta
            result = minuend - subtrahend
            if result < 0:
                print("Error: el resultado es negativo y los números romanos no representan números negativos.")
                return ""
            
            # Convierte el resultado a notación romana
            return self.int_to_roman(result)

# Ejemplo de uso
input_tape = "CD#X"  # Representa "400 - 10"
turing_machine = TuringMachineRomanSubtraction(input_tape)
result = turing_machine.run()
print("Resultado de la resta en números romanos:", result)  # Debería imprimir "CCCXC"
