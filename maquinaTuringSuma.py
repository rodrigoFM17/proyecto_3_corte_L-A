class TuringMachineRomanSum:
    def __init__(self, tape):
        self.tape = tape  # La cinta se recibe como un string
    
    # Diccionario para la conversión de números romanos a enteros
    roman_to_int_mapping = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    
    # Diccionario para la conversión de enteros a números romanos
    int_to_roman_mapping = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    # Convierte un número romano a entero
    def roman_to_int(self, roman):
        total = 0
        prev_value = 0
        for symbol in reversed(roman):
            value = self.roman_to_int_mapping[symbol]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total
    
    # Convierte un entero a número romano
    def int_to_roman(self, num):
        roman = []
        for value, symbol in self.int_to_roman_mapping:
            while num >= value:
                roman.append(symbol)
                num -= value
        return "".join(roman)
    
    # Ejecuta la suma de números romanos
    def run(self):
        # Divide la cinta en los dos números romanos
        num1, num2 = self.tape.split("#")
        
        # Convierte ambos números romanos a enteros y los suma
        result_int = self.roman_to_int(num1) + self.roman_to_int(num2)
        
        # Convierte el resultado de la suma de vuelta a número romano
        return self.int_to_roman(result_int)

# Ejemplo de uso
input_tape = "LXIX#XX"  # Representa "69 + 20"
turing_machine = TuringMachineRomanSum(input_tape)
result = turing_machine.run()
print("Resultado de la suma en números romanos:", result)
