# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01ca\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u008e\n\3\f\3\16\3\u0091")
        buf.write("\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\7\4\u009a\n\4\f\4\16")
        buf.write("\4\u009d\13\4\3\4\5\4\u00a0\n\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\7\5\u00aa\n\5\f\5\16\5\u00ad\13\5\3\5\3\5\3")
        buf.write("\6\6\6\u00b2\n\6\r\6\16\6\u00b3\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\5\7\u00bc\n\7\3\b\3\b\7\b\u00c0\n\b\f\b\16\b\u00c3")
        buf.write("\13\b\3\t\3\t\3\t\5\t\u00c8\n\t\3\t\6\t\u00cb\n\t\r\t")
        buf.write("\16\t\u00cc\3\n\3\n\5\n\u00d1\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\3$\3$\7$\u015f\n$\f$\16$\u0162\13")
        buf.write("$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3@\3@\3@\3@\3A\3A\3A\3B\3B\3B\3B\7B\u01ac\n")
        buf.write("B\fB\16B\u01af\13B\3B\5B\u01b2\nB\3B\3B\3C\3C\3C\3C\7")
        buf.write("C\u01ba\nC\fC\16C\u01bd\13C\3C\3C\3C\3C\7C\u01c3\nC\f")
        buf.write("C\16C\u01c6\13C\3C\3C\3C\4\u008f\u01c4\2D\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\2\21\2\23\t\25\n\27\13\31\f\33\r\35\16")
        buf.write("\37\17!\20#\21%\22\'\23)\24+\25-\26/\27\61\30\63\31\65")
        buf.write("\32\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,")
        buf.write("[-]._/a\60c\61e\62g\63i\64k\65m\66o\67q8s9u:w;y<{=}>\177")
        buf.write("?\u0081@\u0083A\u0085B\3\2\r\4\2\f\f\17\17\t\2$$^^ddh")
        buf.write("hppttvv\5\2\f\f$$^^\3\2\62;\4\2GGgg\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\5\2\13\f\16\17\"\"\4\2$$^^\3\3\f\f\b\2$$ddhh")
        buf.write("ppttvv\2\u01da\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u0085\3\2\2\2\3\u0087\3\2\2\2\5\u0089\3\2\2\2\7\u0097")
        buf.write("\3\2\2\2\t\u00a5\3\2\2\2\13\u00b1\3\2\2\2\r\u00b5\3\2")
        buf.write("\2\2\17\u00bd\3\2\2\2\21\u00c4\3\2\2\2\23\u00d0\3\2\2")
        buf.write("\2\25\u00d2\3\2\2\2\27\u00d7\3\2\2\2\31\u00db\3\2\2\2")
        buf.write("\33\u00e1\3\2\2\2\35\u00e6\3\2\2\2\37\u00ee\3\2\2\2!\u00f4")
        buf.write("\3\2\2\2#\u00fa\3\2\2\2%\u0101\3\2\2\2\'\u0107\3\2\2\2")
        buf.write(")\u0110\3\2\2\2+\u0113\3\2\2\2-\u0118\3\2\2\2/\u0120\3")
        buf.write("\2\2\2\61\u0123\3\2\2\2\63\u0127\3\2\2\2\65\u012e\3\2")
        buf.write("\2\2\67\u0133\3\2\2\29\u0137\3\2\2\2;\u013e\3\2\2\2=\u0143")
        buf.write("\3\2\2\2?\u0149\3\2\2\2A\u014d\3\2\2\2C\u0152\3\2\2\2")
        buf.write("E\u0155\3\2\2\2G\u015c\3\2\2\2I\u0163\3\2\2\2K\u0165\3")
        buf.write("\2\2\2M\u0167\3\2\2\2O\u0169\3\2\2\2Q\u016b\3\2\2\2S\u016d")
        buf.write("\3\2\2\2U\u016f\3\2\2\2W\u0172\3\2\2\2Y\u0175\3\2\2\2")
        buf.write("[\u0177\3\2\2\2]\u0179\3\2\2\2_\u017c\3\2\2\2a\u017f\3")
        buf.write("\2\2\2c\u0182\3\2\2\2e\u0185\3\2\2\2g\u0187\3\2\2\2i\u0189")
        buf.write("\3\2\2\2k\u018c\3\2\2\2m\u018e\3\2\2\2o\u0190\3\2\2\2")
        buf.write("q\u0192\3\2\2\2s\u0194\3\2\2\2u\u0196\3\2\2\2w\u0198\3")
        buf.write("\2\2\2y\u019a\3\2\2\2{\u019c\3\2\2\2}\u019e\3\2\2\2\177")
        buf.write("\u01a0\3\2\2\2\u0081\u01a4\3\2\2\2\u0083\u01a7\3\2\2\2")
        buf.write("\u0085\u01b5\3\2\2\2\u0087\u0088\7?\2\2\u0088\4\3\2\2")
        buf.write("\2\u0089\u008a\7\61\2\2\u008a\u008b\7,\2\2\u008b\u008f")
        buf.write("\3\2\2\2\u008c\u008e\13\2\2\2\u008d\u008c\3\2\2\2\u008e")
        buf.write("\u0091\3\2\2\2\u008f\u0090\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u0090\u0092\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\7")
        buf.write(",\2\2\u0093\u0094\7\61\2\2\u0094\u0095\3\2\2\2\u0095\u0096")
        buf.write("\b\3\2\2\u0096\6\3\2\2\2\u0097\u009b\7%\2\2\u0098\u009a")
        buf.write("\n\2\2\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009f\3\2\2\2")
        buf.write("\u009d\u009b\3\2\2\2\u009e\u00a0\7\17\2\2\u009f\u009e")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1")
        buf.write("\u00a2\7\f\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\b\4\2\2")
        buf.write("\u00a4\b\3\2\2\2\u00a5\u00ab\7$\2\2\u00a6\u00a7\7^\2\2")
        buf.write("\u00a7\u00aa\t\3\2\2\u00a8\u00aa\n\4\2\2\u00a9\u00a6\3")
        buf.write("\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad")
        buf.write("\u00ab\3\2\2\2\u00ae\u00af\7$\2\2\u00af\n\3\2\2\2\u00b0")
        buf.write("\u00b2\t\5\2\2\u00b1\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2")
        buf.write("\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\f\3\2\2")
        buf.write("\2\u00b5\u00bb\5\13\6\2\u00b6\u00bc\5\17\b\2\u00b7\u00bc")
        buf.write("\5\21\t\2\u00b8\u00b9\5\17\b\2\u00b9\u00ba\5\21\t\2\u00ba")
        buf.write("\u00bc\3\2\2\2\u00bb\u00b6\3\2\2\2\u00bb\u00b7\3\2\2\2")
        buf.write("\u00bb\u00b8\3\2\2\2\u00bc\16\3\2\2\2\u00bd\u00c1\5{>")
        buf.write("\2\u00be\u00c0\t\5\2\2\u00bf\u00be\3\2\2\2\u00c0\u00c3")
        buf.write("\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2")
        buf.write("\20\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c7\t\6\2\2\u00c5")
        buf.write("\u00c8\5I%\2\u00c6\u00c8\5K&\2\u00c7\u00c5\3\2\2\2\u00c7")
        buf.write("\u00c6\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00ca\3\2\2\2")
        buf.write("\u00c9\u00cb\t\5\2\2\u00ca\u00c9\3\2\2\2\u00cb\u00cc\3")
        buf.write("\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\22")
        buf.write("\3\2\2\2\u00ce\u00d1\5;\36\2\u00cf\u00d1\5=\37\2\u00d0")
        buf.write("\u00ce\3\2\2\2\u00d0\u00cf\3\2\2\2\u00d1\24\3\2\2\2\u00d2")
        buf.write("\u00d3\7o\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7k\2\2\u00d5")
        buf.write("\u00d6\7p\2\2\u00d6\26\3\2\2\2\u00d7\u00d8\7k\2\2\u00d8")
        buf.write("\u00d9\7p\2\2\u00d9\u00da\7v\2\2\u00da\30\3\2\2\2\u00db")
        buf.write("\u00dc\7h\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de\7q\2\2\u00de")
        buf.write("\u00df\7c\2\2\u00df\u00e0\7v\2\2\u00e0\32\3\2\2\2\u00e1")
        buf.write("\u00e2\7x\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7k\2\2\u00e4")
        buf.write("\u00e5\7f\2\2\u00e5\34\3\2\2\2\u00e6\u00e7\7d\2\2\u00e7")
        buf.write("\u00e8\7q\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7n\2\2\u00ea")
        buf.write("\u00eb\7g\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7p\2\2\u00ed")
        buf.write("\36\3\2\2\2\u00ee\u00ef\7e\2\2\u00ef\u00f0\7n\2\2\u00f0")
        buf.write("\u00f1\7c\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3\7u\2\2\u00f3")
        buf.write(" \3\2\2\2\u00f4\u00f5\7h\2\2\u00f5\u00f6\7k\2\2\u00f6")
        buf.write("\u00f7\7p\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9\7n\2\2\u00f9")
        buf.write("\"\3\2\2\2\u00fa\u00fb\7u\2\2\u00fb\u00fc\7v\2\2\u00fc")
        buf.write("\u00fd\7c\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7k\2\2\u00ff")
        buf.write("\u0100\7e\2\2\u0100$\3\2\2\2\u0101\u0102\7d\2\2\u0102")
        buf.write("\u0103\7t\2\2\u0103\u0104\7g\2\2\u0104\u0105\7c\2\2\u0105")
        buf.write("\u0106\7m\2\2\u0106&\3\2\2\2\u0107\u0108\7e\2\2\u0108")
        buf.write("\u0109\7q\2\2\u0109\u010a\7p\2\2\u010a\u010b\7v\2\2\u010b")
        buf.write("\u010c\7k\2\2\u010c\u010d\7p\2\2\u010d\u010e\7w\2\2\u010e")
        buf.write("\u010f\7g\2\2\u010f(\3\2\2\2\u0110\u0111\7f\2\2\u0111")
        buf.write("\u0112\7q\2\2\u0112*\3\2\2\2\u0113\u0114\7g\2\2\u0114")
        buf.write("\u0115\7n\2\2\u0115\u0116\7u\2\2\u0116\u0117\7g\2\2\u0117")
        buf.write(",\3\2\2\2\u0118\u0119\7g\2\2\u0119\u011a\7z\2\2\u011a")
        buf.write("\u011b\7v\2\2\u011b\u011c\7g\2\2\u011c\u011d\7p\2\2\u011d")
        buf.write("\u011e\7f\2\2\u011e\u011f\7u\2\2\u011f.\3\2\2\2\u0120")
        buf.write("\u0121\7k\2\2\u0121\u0122\7h\2\2\u0122\60\3\2\2\2\u0123")
        buf.write("\u0124\7p\2\2\u0124\u0125\7g\2\2\u0125\u0126\7y\2\2\u0126")
        buf.write("\62\3\2\2\2\u0127\u0128\7u\2\2\u0128\u0129\7v\2\2\u0129")
        buf.write("\u012a\7t\2\2\u012a\u012b\7k\2\2\u012b\u012c\7p\2\2\u012c")
        buf.write("\u012d\7i\2\2\u012d\64\3\2\2\2\u012e\u012f\7v\2\2\u012f")
        buf.write("\u0130\7j\2\2\u0130\u0131\7g\2\2\u0131\u0132\7p\2\2\u0132")
        buf.write("\66\3\2\2\2\u0133\u0134\7h\2\2\u0134\u0135\7q\2\2\u0135")
        buf.write("\u0136\7t\2\2\u01368\3\2\2\2\u0137\u0138\7t\2\2\u0138")
        buf.write("\u0139\7g\2\2\u0139\u013a\7v\2\2\u013a\u013b\7w\2\2\u013b")
        buf.write("\u013c\7t\2\2\u013c\u013d\7p\2\2\u013d:\3\2\2\2\u013e")
        buf.write("\u013f\7v\2\2\u013f\u0140\7t\2\2\u0140\u0141\7w\2\2\u0141")
        buf.write("\u0142\7g\2\2\u0142<\3\2\2\2\u0143\u0144\7h\2\2\u0144")
        buf.write("\u0145\7c\2\2\u0145\u0146\7n\2\2\u0146\u0147\7u\2\2\u0147")
        buf.write("\u0148\7g\2\2\u0148>\3\2\2\2\u0149\u014a\7p\2\2\u014a")
        buf.write("\u014b\7k\2\2\u014b\u014c\7n\2\2\u014c@\3\2\2\2\u014d")
        buf.write("\u014e\7v\2\2\u014e\u014f\7j\2\2\u014f\u0150\7k\2\2\u0150")
        buf.write("\u0151\7u\2\2\u0151B\3\2\2\2\u0152\u0153\7v\2\2\u0153")
        buf.write("\u0154\7q\2\2\u0154D\3\2\2\2\u0155\u0156\7f\2\2\u0156")
        buf.write("\u0157\7q\2\2\u0157\u0158\7y\2\2\u0158\u0159\7p\2\2\u0159")
        buf.write("\u015a\7v\2\2\u015a\u015b\7q\2\2\u015bF\3\2\2\2\u015c")
        buf.write("\u0160\t\7\2\2\u015d\u015f\t\b\2\2\u015e\u015d\3\2\2\2")
        buf.write("\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3")
        buf.write("\2\2\2\u0161H\3\2\2\2\u0162\u0160\3\2\2\2\u0163\u0164")
        buf.write("\7-\2\2\u0164J\3\2\2\2\u0165\u0166\7/\2\2\u0166L\3\2\2")
        buf.write("\2\u0167\u0168\7,\2\2\u0168N\3\2\2\2\u0169\u016a\7\61")
        buf.write("\2\2\u016aP\3\2\2\2\u016b\u016c\7^\2\2\u016cR\3\2\2\2")
        buf.write("\u016d\u016e\7\'\2\2\u016eT\3\2\2\2\u016f\u0170\7#\2\2")
        buf.write("\u0170\u0171\7?\2\2\u0171V\3\2\2\2\u0172\u0173\7?\2\2")
        buf.write("\u0173\u0174\7?\2\2\u0174X\3\2\2\2\u0175\u0176\7>\2\2")
        buf.write("\u0176Z\3\2\2\2\u0177\u0178\7@\2\2\u0178\\\3\2\2\2\u0179")
        buf.write("\u017a\7>\2\2\u017a\u017b\7?\2\2\u017b^\3\2\2\2\u017c")
        buf.write("\u017d\7@\2\2\u017d\u017e\7?\2\2\u017e`\3\2\2\2\u017f")
        buf.write("\u0180\7~\2\2\u0180\u0181\7~\2\2\u0181b\3\2\2\2\u0182")
        buf.write("\u0183\7(\2\2\u0183\u0184\7(\2\2\u0184d\3\2\2\2\u0185")
        buf.write("\u0186\7#\2\2\u0186f\3\2\2\2\u0187\u0188\7`\2\2\u0188")
        buf.write("h\3\2\2\2\u0189\u018a\7<\2\2\u018a\u018b\7?\2\2\u018b")
        buf.write("j\3\2\2\2\u018c\u018d\7]\2\2\u018dl\3\2\2\2\u018e\u018f")
        buf.write("\7_\2\2\u018fn\3\2\2\2\u0190\u0191\7}\2\2\u0191p\3\2\2")
        buf.write("\2\u0192\u0193\7\177\2\2\u0193r\3\2\2\2\u0194\u0195\7")
        buf.write("*\2\2\u0195t\3\2\2\2\u0196\u0197\7+\2\2\u0197v\3\2\2\2")
        buf.write("\u0198\u0199\7=\2\2\u0199x\3\2\2\2\u019a\u019b\7<\2\2")
        buf.write("\u019bz\3\2\2\2\u019c\u019d\7\60\2\2\u019d|\3\2\2\2\u019e")
        buf.write("\u019f\7.\2\2\u019f~\3\2\2\2\u01a0\u01a1\t\t\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a3\b@\2\2\u01a3\u0080\3\2\2\2")
        buf.write("\u01a4\u01a5\13\2\2\2\u01a5\u01a6\bA\3\2\u01a6\u0082\3")
        buf.write("\2\2\2\u01a7\u01ad\7$\2\2\u01a8\u01a9\7^\2\2\u01a9\u01ac")
        buf.write("\t\3\2\2\u01aa\u01ac\n\n\2\2\u01ab\u01a8\3\2\2\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3")
        buf.write("\2\2\2\u01b0\u01b2\t\13\2\2\u01b1\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3\u01b4\bB\4\2\u01b4\u0084\3\2\2\2")
        buf.write("\u01b5\u01bb\7$\2\2\u01b6\u01ba\n\n\2\2\u01b7\u01b8\7")
        buf.write("^\2\2\u01b8\u01ba\t\3\2\2\u01b9\u01b6\3\2\2\2\u01b9\u01b7")
        buf.write("\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2")
        buf.write("\u01be\u01bf\7^\2\2\u01bf\u01c0\n\f\2\2\u01c0\u01c4\3")
        buf.write("\2\2\2\u01c1\u01c3\13\2\2\2\u01c2\u01c1\3\2\2\2\u01c3")
        buf.write("\u01c6\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c4\u01c2\3\2\2\2")
        buf.write("\u01c5\u01c7\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c8\7")
        buf.write("$\2\2\u01c8\u01c9\bC\5\2\u01c9\u0086\3\2\2\2\25\2\u008f")
        buf.write("\u009b\u009f\u00a9\u00ab\u00b3\u00bb\u00c1\u00c7\u00cc")
        buf.write("\u00d0\u0160\u01ab\u01ad\u01b1\u01b9\u01bb\u01c4\6\b\2")
        buf.write("\2\3A\2\3B\3\3C\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    COMMENT = 2
    LINE_COMMENT = 3
    STRINGMT = 4
    INTMT = 5
    FLOATMT = 6
    BOOLMT = 7
    MAIN_LIT = 8
    INT_LIT = 9
    FLOAT_LIT = 10
    VOID_LIT = 11
    BOOL_LIT = 12
    CLASS_LIT = 13
    FINAL_LIT = 14
    STATIC_LIT = 15
    BREAK_LIT = 16
    CONT_LIT = 17
    DO_LIT = 18
    ELSE_LIT = 19
    EXTEND_LIT = 20
    IF_LIT = 21
    NEW_LIT = 22
    STRING_LIT = 23
    THEN_LIT = 24
    FOR_LIT = 25
    RETURN_LIT = 26
    TRUE_LIT = 27
    FALSE_LIT = 28
    NIL_LIT = 29
    THIS_LIT = 30
    TO_LIT = 31
    DOWNTO_LIT = 32
    ID = 33
    ADD_OP = 34
    SUB_OP = 35
    MUL_OP = 36
    FLOAT_DIV_OP = 37
    INT_DIV_OP = 38
    MOD_OP = 39
    NEQUA_OP = 40
    ISEQUA_OP = 41
    LESS_OP = 42
    GREAT_OP = 43
    LEQUA_OP = 44
    GEQUA_OP = 45
    OR_OP = 46
    AND_OP = 47
    NOT_OP = 48
    CONCAT_OP = 49
    ASSIGN_OP = 50
    LSB = 51
    RSB = 52
    LCB = 53
    RCB = 54
    LB = 55
    RB = 56
    SEMI = 57
    COLON = 58
    DOT = 59
    COMMA = 60
    WS = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'main'", "'int'", "'float'", "'void'", "'boolean'", 
            "'class'", "'final'", "'static'", "'break'", "'continue'", "'do'", 
            "'else'", "'extends'", "'if'", "'new'", "'string'", "'then'", 
            "'for'", "'return'", "'true'", "'false'", "'nil'", "'this'", 
            "'to'", "'downto'", "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", 
            "'!='", "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", 
            "'!'", "'^'", "':='", "'['", "']'", "'{'", "'}'", "'('", "')'", 
            "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "LINE_COMMENT", "STRINGMT", "INTMT", "FLOATMT", "BOOLMT", 
            "MAIN_LIT", "INT_LIT", "FLOAT_LIT", "VOID_LIT", "BOOL_LIT", 
            "CLASS_LIT", "FINAL_LIT", "STATIC_LIT", "BREAK_LIT", "CONT_LIT", 
            "DO_LIT", "ELSE_LIT", "EXTEND_LIT", "IF_LIT", "NEW_LIT", "STRING_LIT", 
            "THEN_LIT", "FOR_LIT", "RETURN_LIT", "TRUE_LIT", "FALSE_LIT", 
            "NIL_LIT", "THIS_LIT", "TO_LIT", "DOWNTO_LIT", "ID", "ADD_OP", 
            "SUB_OP", "MUL_OP", "FLOAT_DIV_OP", "INT_DIV_OP", "MOD_OP", 
            "NEQUA_OP", "ISEQUA_OP", "LESS_OP", "GREAT_OP", "LEQUA_OP", 
            "GEQUA_OP", "OR_OP", "AND_OP", "NOT_OP", "CONCAT_OP", "ASSIGN_OP", 
            "LSB", "RSB", "LCB", "RCB", "LB", "RB", "SEMI", "COLON", "DOT", 
            "COMMA", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "COMMENT", "LINE_COMMENT", "STRINGMT", "INTMT", 
                  "FLOATMT", "DECIMALPT", "EXPONENTPT", "BOOLMT", "MAIN_LIT", 
                  "INT_LIT", "FLOAT_LIT", "VOID_LIT", "BOOL_LIT", "CLASS_LIT", 
                  "FINAL_LIT", "STATIC_LIT", "BREAK_LIT", "CONT_LIT", "DO_LIT", 
                  "ELSE_LIT", "EXTEND_LIT", "IF_LIT", "NEW_LIT", "STRING_LIT", 
                  "THEN_LIT", "FOR_LIT", "RETURN_LIT", "TRUE_LIT", "FALSE_LIT", 
                  "NIL_LIT", "THIS_LIT", "TO_LIT", "DOWNTO_LIT", "ID", "ADD_OP", 
                  "SUB_OP", "MUL_OP", "FLOAT_DIV_OP", "INT_DIV_OP", "MOD_OP", 
                  "NEQUA_OP", "ISEQUA_OP", "LESS_OP", "GREAT_OP", "LEQUA_OP", 
                  "GEQUA_OP", "OR_OP", "AND_OP", "NOT_OP", "CONCAT_OP", 
                  "ASSIGN_OP", "LSB", "RSB", "LCB", "RCB", "LB", "RB", "SEMI", 
                  "COLON", "DOT", "COMMA", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[63] = self.ERROR_CHAR_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text)
     


