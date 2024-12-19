from LEGOParser import *
from LEGOListener import LEGOListener

class LegoToPython(LEGOListener):
    # Inicializa la clase con una lista para el código Python y el nivel de indentación
    def __init__(self):
        self.python_code = []
        self.indent_level = 0

    # Agrega una línea al código Python con la indentación adecuada
    def add_line(self, line):
        indent = "    " * self.indent_level
        self.python_code.append(f"{indent}{line}")

    # Escribe el código generado en un archivo de salida
    def write_to_file(self, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(self.python_code))

    # Método que se llama al ingresar un programa, inicia el código Python
    def enterPrograma(self, ctx: LEGOParser.ProgramaContext):
        self.add_line("# Código generado desde LEGO")
        self.add_line("def main():")
        self.indent_level += 1

    # Método que se llama al salir del programa, finaliza el código Python
    def exitPrograma(self, ctx: LEGOParser.ProgramaContext):
        self.indent_level -= 1
        self.python_code.append("")
        self.indent_level -= 1
        self.add_line("if __name__ == '__main__':")
        self.add_line("    main()")

    # Método que maneja la instrucción "MOSTRAR_LEGO" en el código LEGO
    def enterMostrarInstruccion(self, ctx: LEGOParser.MostrarInstruccionContext):
        if ctx.PALABRA_BLOQUE() is not None and ctx.IDENTIFICADOR() is not None:
            expr1 = ctx.PALABRA_BLOQUE().getText()
            expr2 = ctx.IDENTIFICADOR().getText()
            self.add_line(f"print({expr1}, {expr2})")
        elif ctx.PALABRA_BLOQUE() is not None:
            expr = ctx.PALABRA_BLOQUE().getText()
            self.add_line(f"print({expr})")
        elif ctx.IDENTIFICADOR() is not None:
            var_name = ctx.IDENTIFICADOR().getText()
            self.add_line(f"print({var_name})")
        else:
            raise ValueError("No se pudo determinar el tipo de argumento para MOSTRAR_LEGO.")

    # Método que maneja la instrucción "PEDIR_LEGO" en el código LEGO
    def enterPedirInstruccion(self, ctx: LEGOParser.PedirInstruccionContext):
        prompt = ctx.PALABRA_BLOQUE().getText().strip('"')
        var_name = ctx.IDENTIFICADOR().getText()
        self.add_line(f"{var_name} = int(input('{prompt}: '))")

    # Método que maneja la instrucción de asignación en el código LEGO
    def enterAsignacionInstruccion(self, ctx: LEGOParser.AsignacionInstruccionContext):
        var_name = ctx.IDENTIFICADOR().getText()
        expr = self.convertirExpresion(ctx.expresion())
        self.add_line(f"{var_name} = {expr}")

    # Método que maneja la instrucción "REPETIR_LEGO" en el código LEGO
    def enterRepetirInstruccion(self, ctx: LEGOParser.RepetirInstruccionContext):
        times = self.convertirExpresion(ctx.expresion())
        self.add_line(f"for _ in range({times}):")
        self.indent_level += 1

    # Método que maneja el fin del bucle "REPETIR_LEGO"
    def exitRepetirInstruccion(self, ctx: LEGOParser.RepetirInstruccionContext):
        self.indent_level -= 1

    # Método que maneja la instrucción "CONDICION_INSTRUCCION" en el código LEGO
    def enterCondicionInstruccion(self, ctx: LEGOParser.CondicionInstruccionContext):
        cond = ctx.condicion()
        
        if cond.getChildCount() < 3:
            raise ValueError("Condición incompleta: se esperaban dos expresiones y un operador.")
        
        left = self.convertirExpresion(cond.expresion(0))
        right = self.convertirExpresion(cond.expresion(1))
        
        operadores_python = {
            "MAS_GRANDE_QUE": ">",
            "MAS_PEQUE_QUE": "<",
            "ESTE_BLOQUE_IGUAL_A": "==",
            "DIFERENTE_A": "!=",
        }
        
        operador_logico = cond.operadorLog().getText() if cond.operadorLog() else None
        operador = operadores_python.get(operador_logico)
        
        if operador is None:
            raise ValueError(f"Operador lógico desconocido: {operador_logico}")
        
        self.add_line(f"if ({left} {operador} {right}):")
        self.indent_level += 1

    # Método que maneja el fin de una instrucción condicional con "SINO"
    def exitCondicionInstruccion(self, ctx: LEGOParser.CondicionInstruccionContext):
        self.indent_level -= 1  
        if ctx.SINO() is not None:  
            self.add_line("else:")
            self.indent_level += 1

    # Método que maneja la instrucción "MIENTRAS_APILO" en el código LEGO
    def enterMientrasApiloInstruccion(self, ctx: LEGOParser.MientrasApiloInstruccionContext):
        cond = ctx.condicion()
        left = self.convertirExpresion(cond.expresion(0))
        right = self.convertirExpresion(cond.expresion(1))
        
        operadores_python = {
            "MAS_GRANDE_QUE": ">",
            "MAS_PEQUE_QUE": "<",
            "ESTE_BLOQUE_IGUAL_A": "==",
            "DIFERENTE_A": "!=",
        }

        operador_logico = cond.operadorLog().getText() if cond.operadorLog() else None
        operador = operadores_python.get(operador_logico)
        
        if operador is None:
            raise ValueError(f"Operador lógico desconocido: {operador_logico}")
        
        self.add_line(f"while ({left} {operador} {right}):")
        self.indent_level += 1

    # Método que maneja el fin del bucle "MIENTRAS_APILO"
    def exitMientrasApiloInstruccion(self, ctx: LEGOParser.MientrasApiloInstruccionContext):
        self.indent_level -= 1

    # Método para convertir una expresión en código Python
    def convertirExpresion(self, ctx: LEGOParser.ExpresionContext):
        if ctx.term():
            terms = [self.convertirTerm(ctx.term(i)) for i in range(len(ctx.term()))]
            operadores = [ctx.operadorMat(i).getText() for i in range(len(ctx.operadorMat()))]

            operadores_python = {
                "AGREGAR_BLOQUE": "+",
                "QUITAR_BLOQUE": "-",
                "APILAR_BLOQUES": "*",
                "DIVIDIR_BLOQUES": "/",
                "POTENCIAR_BLOQUES": "**",
            }

            # Construir la expresión completa
            resultado = terms[0]
            for i, operador in enumerate(operadores):
                operador_python = operadores_python.get(operador)
                if operador_python is None:
                    raise ValueError(f"Operador desconocido: {operador}")
                resultado = f"({resultado} {operador_python} {terms[i + 1]})"

            return resultado
        else:
            raise ValueError("La expresión no contiene términos válidos.")

    # Método para convertir un término en código Python
    def convertirTerm(self, ctx: LEGOParser.TermContext):
        if ctx.factor():
            factors = [self.convertirFactor(ctx.factor(i)) for i in range(len(ctx.factor()))]
            operadores = [ctx.operadorMat(i).getText() for i in range(len(ctx.operadorMat()))]

            operadores_python = {
                "AGREGAR_BLOQUE": "+",
                "QUITAR_BLOQUE": "-",
                "APILAR_BLOQUES": "*",
                "DIVIDIR_BLOQUES": "/",
                "POTENCIAR_BLOQUES": "**",
            }

            resultado = factors[0]
            for i, operador in enumerate(operadores):
                operador_python = operadores_python.get(operador)
                if operador_python is None:
                    raise ValueError(f"Operador desconocido: {operador}")
                resultado = f"({resultado} {operador_python} {factors[i + 1]})"

            return resultado
        else:
            raise ValueError("El término no contiene factores válidos.")

    # Método para convertir un factor en código Python
    def convertirFactor(self, ctx: LEGOParser.FactorContext):
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.IDENTIFICADOR():
            return ctx.IDENTIFICADOR().getText()
        elif ctx.expresion():
            return f"({self.convertirExpresion(ctx.expresion())})"
        else:
            raise ValueError(f"Factor inesperado: {ctx.getText()}")
