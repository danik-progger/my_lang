// Generated from /home/dan/Desktop/dev/mipt/my-lang/antlr/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		SPACES=10, FUN=11, MAIN=12, NEWLINE=13, INT=14, PRINT=15, IF=16, ELSE=17, 
		WHILE=18, IDENT=19;
	public static final int
		RULE_prog = 0, RULE_stmt = 1, RULE_expr = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "stmt", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "'='", "'*'", "'/'", "'+'", "'-'", 
			null, "'fun'", "'main'", null, null, "'print '", "'if '", "'else'", "'while'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "SPACES", 
			"FUN", "MAIN", "NEWLINE", "INT", "PRINT", "IF", "ELSE", "WHILE", "IDENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public TerminalNode FUN() { return getToken(ExprParser.FUN, 0); }
		public TerminalNode MAIN() { return getToken(ExprParser.MAIN, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(ExprParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ExprParser.NEWLINE, i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(6);
			match(FUN);
			setState(7);
			match(MAIN);
			setState(8);
			match(T__0);
			setState(9);
			match(T__1);
			setState(10);
			match(T__2);
			setState(11);
			match(NEWLINE);
			{
			setState(17);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 622592L) != 0)) {
				{
				{
				setState(12);
				stmt();
				setState(13);
				match(NEWLINE);
				}
				}
				setState(19);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
			setState(20);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtContext extends ParserRuleContext {
		public ExprContext printexp;
		public ExprContext exp;
		public Token ident;
		public ExprContext assign;
		public TerminalNode PRINT() { return getToken(ExprParser.PRINT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode IF() { return getToken(ExprParser.IF, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(ExprParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ExprParser.NEWLINE, i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public TerminalNode IDENT() { return getToken(ExprParser.IDENT, 0); }
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stmt);
		int _la;
		try {
			setState(44);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRINT:
				enterOuterAlt(_localctx, 1);
				{
				setState(22);
				match(PRINT);
				setState(23);
				match(T__0);
				setState(24);
				((StmtContext)_localctx).printexp = expr(0);
				setState(25);
				match(T__1);
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 2);
				{
				setState(27);
				match(IF);
				setState(28);
				((StmtContext)_localctx).exp = expr(0);
				setState(29);
				match(T__2);
				setState(30);
				match(NEWLINE);
				{
				setState(36);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 622592L) != 0)) {
					{
					{
					setState(31);
					stmt();
					setState(32);
					match(NEWLINE);
					}
					}
					setState(38);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				setState(39);
				match(T__3);
				}
				break;
			case IDENT:
				enterOuterAlt(_localctx, 3);
				{
				setState(41);
				((StmtContext)_localctx).ident = match(IDENT);
				{
				setState(42);
				match(T__4);
				}
				setState(43);
				((StmtContext)_localctx).assign = expr(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public Token value;
		public ExprContext exp;
		public Token ident;
		public Token op;
		public TerminalNode INT() { return getToken(ExprParser.INT, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode IDENT() { return getToken(ExprParser.IDENT, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				setState(47);
				((ExprContext)_localctx).value = match(INT);
				}
				break;
			case T__0:
				{
				setState(48);
				match(T__0);
				setState(49);
				((ExprContext)_localctx).exp = expr(0);
				setState(50);
				match(T__1);
				}
				break;
			case IDENT:
				{
				setState(52);
				((ExprContext)_localctx).ident = match(IDENT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(63);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(61);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(55);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(56);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__5 || _la==T__6) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(57);
						expr(6);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(58);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(59);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__7 || _la==T__8) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(60);
						expr(5);
						}
						break;
					}
					} 
				}
				setState(65);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0013C\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u0000\u0010"+
		"\b\u0000\n\u0000\f\u0000\u0013\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001"+
		"#\b\u0001\n\u0001\f\u0001&\t\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u0001-\b\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002"+
		"6\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0005\u0002>\b\u0002\n\u0002\f\u0002A\t\u0002\u0001\u0002"+
		"\u0000\u0001\u0004\u0003\u0000\u0002\u0004\u0000\u0002\u0001\u0000\u0006"+
		"\u0007\u0001\u0000\b\tG\u0000\u0006\u0001\u0000\u0000\u0000\u0002,\u0001"+
		"\u0000\u0000\u0000\u00045\u0001\u0000\u0000\u0000\u0006\u0007\u0005\u000b"+
		"\u0000\u0000\u0007\b\u0005\f\u0000\u0000\b\t\u0005\u0001\u0000\u0000\t"+
		"\n\u0005\u0002\u0000\u0000\n\u000b\u0005\u0003\u0000\u0000\u000b\u0011"+
		"\u0005\r\u0000\u0000\f\r\u0003\u0002\u0001\u0000\r\u000e\u0005\r\u0000"+
		"\u0000\u000e\u0010\u0001\u0000\u0000\u0000\u000f\f\u0001\u0000\u0000\u0000"+
		"\u0010\u0013\u0001\u0000\u0000\u0000\u0011\u000f\u0001\u0000\u0000\u0000"+
		"\u0011\u0012\u0001\u0000\u0000\u0000\u0012\u0014\u0001\u0000\u0000\u0000"+
		"\u0013\u0011\u0001\u0000\u0000\u0000\u0014\u0015\u0005\u0004\u0000\u0000"+
		"\u0015\u0001\u0001\u0000\u0000\u0000\u0016\u0017\u0005\u000f\u0000\u0000"+
		"\u0017\u0018\u0005\u0001\u0000\u0000\u0018\u0019\u0003\u0004\u0002\u0000"+
		"\u0019\u001a\u0005\u0002\u0000\u0000\u001a-\u0001\u0000\u0000\u0000\u001b"+
		"\u001c\u0005\u0010\u0000\u0000\u001c\u001d\u0003\u0004\u0002\u0000\u001d"+
		"\u001e\u0005\u0003\u0000\u0000\u001e$\u0005\r\u0000\u0000\u001f \u0003"+
		"\u0002\u0001\u0000 !\u0005\r\u0000\u0000!#\u0001\u0000\u0000\u0000\"\u001f"+
		"\u0001\u0000\u0000\u0000#&\u0001\u0000\u0000\u0000$\"\u0001\u0000\u0000"+
		"\u0000$%\u0001\u0000\u0000\u0000%\'\u0001\u0000\u0000\u0000&$\u0001\u0000"+
		"\u0000\u0000\'(\u0005\u0004\u0000\u0000(-\u0001\u0000\u0000\u0000)*\u0005"+
		"\u0013\u0000\u0000*+\u0005\u0005\u0000\u0000+-\u0003\u0004\u0002\u0000"+
		",\u0016\u0001\u0000\u0000\u0000,\u001b\u0001\u0000\u0000\u0000,)\u0001"+
		"\u0000\u0000\u0000-\u0003\u0001\u0000\u0000\u0000./\u0006\u0002\uffff"+
		"\uffff\u0000/6\u0005\u000e\u0000\u000001\u0005\u0001\u0000\u000012\u0003"+
		"\u0004\u0002\u000023\u0005\u0002\u0000\u000036\u0001\u0000\u0000\u0000"+
		"46\u0005\u0013\u0000\u00005.\u0001\u0000\u0000\u000050\u0001\u0000\u0000"+
		"\u000054\u0001\u0000\u0000\u00006?\u0001\u0000\u0000\u000078\n\u0005\u0000"+
		"\u000089\u0007\u0000\u0000\u00009>\u0003\u0004\u0002\u0006:;\n\u0004\u0000"+
		"\u0000;<\u0007\u0001\u0000\u0000<>\u0003\u0004\u0002\u0005=7\u0001\u0000"+
		"\u0000\u0000=:\u0001\u0000\u0000\u0000>A\u0001\u0000\u0000\u0000?=\u0001"+
		"\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000@\u0005\u0001\u0000\u0000"+
		"\u0000A?\u0001\u0000\u0000\u0000\u0006\u0011$,5=?";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}