# Generated from Expr.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,67,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,35,8,1,10,1,12,1,38,9,1,1,1,1,1,1,
        1,1,1,1,1,3,1,45,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,54,8,2,1,2,
        1,2,1,2,1,2,1,2,1,2,5,2,62,8,2,10,2,12,2,65,9,2,1,2,0,1,4,3,0,2,
        4,0,2,1,0,6,7,1,0,8,9,71,0,6,1,0,0,0,2,44,1,0,0,0,4,53,1,0,0,0,6,
        7,5,11,0,0,7,8,5,12,0,0,8,9,5,1,0,0,9,10,5,2,0,0,10,11,5,3,0,0,11,
        17,5,13,0,0,12,13,3,2,1,0,13,14,5,13,0,0,14,16,1,0,0,0,15,12,1,0,
        0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,20,1,0,0,0,19,17,
        1,0,0,0,20,21,5,4,0,0,21,1,1,0,0,0,22,23,5,15,0,0,23,24,5,1,0,0,
        24,25,3,4,2,0,25,26,5,2,0,0,26,45,1,0,0,0,27,28,5,16,0,0,28,29,3,
        4,2,0,29,30,5,3,0,0,30,36,5,13,0,0,31,32,3,2,1,0,32,33,5,13,0,0,
        33,35,1,0,0,0,34,31,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,
        0,0,0,37,39,1,0,0,0,38,36,1,0,0,0,39,40,5,4,0,0,40,45,1,0,0,0,41,
        42,5,19,0,0,42,43,5,5,0,0,43,45,3,4,2,0,44,22,1,0,0,0,44,27,1,0,
        0,0,44,41,1,0,0,0,45,3,1,0,0,0,46,47,6,2,-1,0,47,54,5,14,0,0,48,
        49,5,1,0,0,49,50,3,4,2,0,50,51,5,2,0,0,51,54,1,0,0,0,52,54,5,19,
        0,0,53,46,1,0,0,0,53,48,1,0,0,0,53,52,1,0,0,0,54,63,1,0,0,0,55,56,
        10,5,0,0,56,57,7,0,0,0,57,62,3,4,2,6,58,59,10,4,0,0,59,60,7,1,0,
        0,60,62,3,4,2,5,61,55,1,0,0,0,61,58,1,0,0,0,62,65,1,0,0,0,63,61,
        1,0,0,0,63,64,1,0,0,0,64,5,1,0,0,0,65,63,1,0,0,0,6,17,36,44,53,61,
        63
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'='", "'*'", 
                     "'/'", "'+'", "'-'", "<INVALID>", "'fun'", "'main'", 
                     "<INVALID>", "<INVALID>", "'print '", "'if '", "'else'", 
                     "'while'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SPACES", "FUN", "MAIN", 
                      "NEWLINE", "INT", "PRINT", "IF", "ELSE", "WHILE", 
                      "IDENT" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stmt", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    SPACES=10
    FUN=11
    MAIN=12
    NEWLINE=13
    INT=14
    PRINT=15
    IF=16
    ELSE=17
    WHILE=18
    IDENT=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUN(self):
            return self.getToken(ExprParser.FUN, 0)

        def MAIN(self):
            return self.getToken(ExprParser.MAIN, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StmtContext)
            else:
                return self.getTypedRuleContext(ExprParser.StmtContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(ExprParser.FUN)
            self.state = 7
            self.match(ExprParser.MAIN)
            self.state = 8
            self.match(ExprParser.T__0)
            self.state = 9
            self.match(ExprParser.T__1)
            self.state = 10
            self.match(ExprParser.T__2)
            self.state = 11
            self.match(ExprParser.NEWLINE)

            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 622592) != 0):
                self.state = 12
                self.stmt()
                self.state = 13
                self.match(ExprParser.NEWLINE)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(ExprParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.printexp = None # ExprContext
            self.exp = None # ExprContext
            self.ident = None # Token
            self.assign = None # ExprContext

        def PRINT(self):
            return self.getToken(ExprParser.PRINT, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StmtContext)
            else:
                return self.getTypedRuleContext(ExprParser.StmtContext,i)


        def IDENT(self):
            return self.getToken(ExprParser.IDENT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = ExprParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(ExprParser.PRINT)
                self.state = 23
                self.match(ExprParser.T__0)
                self.state = 24
                localctx.printexp = self.expr(0)
                self.state = 25
                self.match(ExprParser.T__1)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(ExprParser.IF)
                self.state = 28
                localctx.exp = self.expr(0)
                self.state = 29
                self.match(ExprParser.T__2)
                self.state = 30
                self.match(ExprParser.NEWLINE)

                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 622592) != 0):
                    self.state = 31
                    self.stmt()
                    self.state = 32
                    self.match(ExprParser.NEWLINE)
                    self.state = 38
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 39
                self.match(ExprParser.T__3)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                localctx.ident = self.match(ExprParser.IDENT)

                self.state = 42
                self.match(ExprParser.T__4)
                self.state = 43
                localctx.assign = self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None # Token
            self.exp = None # ExprContext
            self.ident = None # Token
            self.op = None # Token

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def IDENT(self):
            return self.getToken(ExprParser.IDENT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 47
                localctx.value = self.match(ExprParser.INT)
                pass
            elif token in [1]:
                self.state = 48
                self.match(ExprParser.T__0)
                self.state = 49
                localctx.exp = self.expr(0)
                self.state = 50
                self.match(ExprParser.T__1)
                pass
            elif token in [19]:
                self.state = 52
                localctx.ident = self.match(ExprParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 61
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 56
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 59
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        self.expr(5)
                        pass

             
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




