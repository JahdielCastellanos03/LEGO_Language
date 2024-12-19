from antlr4 import *
from LEGOParser import LEGOParser
from LEGOLexer import LEGOLexer
from LegoToPython import LegoToPython

def main():
    input_file = "ejemplo.toycode"
    output_file = "output.py"

    try:
        input_stream = FileStream(input_file, encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: El archivo {input_file} no existe.")
        return

    lexer = LEGOLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LEGOParser(token_stream)

    try:
        tree = parser.programa()
    except Exception as e:
        print(f"Error al analizar el archivo: {e}")
        return

    translator = LegoToPython()
    walker = ParseTreeWalker()

    try:
        walker.walk(translator, tree)
    except Exception as e:
        print(f"Error durante la traducción: {e}")
        return

    try:
        translator.write_to_file(output_file)
        print(f"Código generado exitosamente en {output_file}")
    except Exception as e:
        print(f"Error al escribir el archivo {output_file}: {e}")

if __name__ == "__main__":
    main()