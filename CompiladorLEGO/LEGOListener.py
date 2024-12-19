# Generated from LEGO.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LEGOParser import LEGOParser
else:
    from LEGOParser import LEGOParser

# This class defines a complete listener for a parse tree produced by LEGOParser.
class LEGOListener(ParseTreeListener):

    # Enter a parse tree produced by LEGOParser#programa.
    def enterPrograma(self, ctx:LEGOParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LEGOParser#programa.
    def exitPrograma(self, ctx:LEGOParser.ProgramaContext):
        pass


    # Enter a parse tree produced by LEGOParser#bloque.
    def enterBloque(self, ctx:LEGOParser.BloqueContext):
        pass

    # Exit a parse tree produced by LEGOParser#bloque.
    def exitBloque(self, ctx:LEGOParser.BloqueContext):
        pass


    # Enter a parse tree produced by LEGOParser#instruccion.
    def enterInstruccion(self, ctx:LEGOParser.InstruccionContext):
        pass

    # Exit a parse tree produced by LEGOParser#instruccion.
    def exitInstruccion(self, ctx:LEGOParser.InstruccionContext):
        pass


    # Enter a parse tree produced by LEGOParser#asignacionInstruccion.
    def enterAsignacionInstruccion(self, ctx:LEGOParser.AsignacionInstruccionContext):
        pass

    # Exit a parse tree produced by LEGOParser#asignacionInstruccion.
    def exitAsignacionInstruccion(self, ctx:LEGOParser.AsignacionInstruccionContext):
        pass


    # Enter a parse tree produced by LEGOParser#mostrarInstruccion.
    def enterMostrarInstruccion(self, ctx:LEGOParser.MostrarInstruccionContext):
        pass

    # Exit a parse tree produced by LEGOParser#mostrarInstruccion.
    def exitMostrarInstruccion(self, ctx:LEGOParser.MostrarInstruccionContext):
        pass


    # Enter a parse tree produced by LEGOParser#pedirInstruccion.
    def enterPedirInstruccion(self, ctx:LEGOParser.PedirInstruccionContext):
        pass

    # Exit a parse tree produced by LEGOParser#pedirInstruccion.
    def exitPedirInstruccion(self, ctx:LEGOParser.PedirInstruccionContext):
        pass


    # Enter a parse tree produced by LEGOParser#repetirInstruccion.
    def enterRepetirInstruccion(self, ctx:LEGOParser.RepetirInstruccionContext):
        pass

    # Exit a parse tree produced by LEGOParser#repetirInstruccion.
    def exitRepetirInstruccion(self, ctx:LEGOParser.RepetirInstruccionContext):
        pass


    # Enter a parse tree produced by LEGOParser#condicionInstruccion.
    def enterCondicionInstruccion(self, ctx:LEGOParser.CondicionInstruccionContext):
        pass

    # Exit a parse tree produced by LEGOParser#condicionInstruccion.
    def exitCondicionInstruccion(self, ctx:LEGOParser.CondicionInstruccionContext):
        pass


    # Enter a parse tree produced by LEGOParser#mientrasApiloInstruccion.
    def enterMientrasApiloInstruccion(self, ctx:LEGOParser.MientrasApiloInstruccionContext):
        pass

    # Exit a parse tree produced by LEGOParser#mientrasApiloInstruccion.
    def exitMientrasApiloInstruccion(self, ctx:LEGOParser.MientrasApiloInstruccionContext):
        pass


    # Enter a parse tree produced by LEGOParser#operacionInstruccion.
    def enterOperacionInstruccion(self, ctx:LEGOParser.OperacionInstruccionContext):
        pass

    # Exit a parse tree produced by LEGOParser#operacionInstruccion.
    def exitOperacionInstruccion(self, ctx:LEGOParser.OperacionInstruccionContext):
        pass


    # Enter a parse tree produced by LEGOParser#expresion.
    def enterExpresion(self, ctx:LEGOParser.ExpresionContext):
        pass

    # Exit a parse tree produced by LEGOParser#expresion.
    def exitExpresion(self, ctx:LEGOParser.ExpresionContext):
        pass


    # Enter a parse tree produced by LEGOParser#term.
    def enterTerm(self, ctx:LEGOParser.TermContext):
        pass

    # Exit a parse tree produced by LEGOParser#term.
    def exitTerm(self, ctx:LEGOParser.TermContext):
        pass


    # Enter a parse tree produced by LEGOParser#factor.
    def enterFactor(self, ctx:LEGOParser.FactorContext):
        pass

    # Exit a parse tree produced by LEGOParser#factor.
    def exitFactor(self, ctx:LEGOParser.FactorContext):
        pass


    # Enter a parse tree produced by LEGOParser#condicion.
    def enterCondicion(self, ctx:LEGOParser.CondicionContext):
        pass

    # Exit a parse tree produced by LEGOParser#condicion.
    def exitCondicion(self, ctx:LEGOParser.CondicionContext):
        pass


    # Enter a parse tree produced by LEGOParser#operadorLog.
    def enterOperadorLog(self, ctx:LEGOParser.OperadorLogContext):
        pass

    # Exit a parse tree produced by LEGOParser#operadorLog.
    def exitOperadorLog(self, ctx:LEGOParser.OperadorLogContext):
        pass


    # Enter a parse tree produced by LEGOParser#operadorMat.
    def enterOperadorMat(self, ctx:LEGOParser.OperadorMatContext):
        pass

    # Exit a parse tree produced by LEGOParser#operadorMat.
    def exitOperadorMat(self, ctx:LEGOParser.OperadorMatContext):
        pass



del LEGOParser