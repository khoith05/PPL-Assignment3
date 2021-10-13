# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u01dd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3p\n\3\3\4\3\4\3\4\3\4")
        buf.write("\5\4v\n\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u0080\n")
        buf.write("\5\3\6\3\6\3\6\5\6\u0085\n\6\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\t\u0096\n\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a2\n\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00a9\n\13\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00b9")
        buf.write("\n\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\5\20\u00c2\n")
        buf.write("\20\3\21\3\21\3\21\3\21\5\21\u00c8\n\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u00cf\n\22\3\22\3\22\3\22\3\23\3\23\5")
        buf.write("\23\u00d6\n\23\3\24\3\24\3\24\3\24\3\24\5\24\u00dd\n\24")
        buf.write("\3\25\3\25\5\25\u00e1\n\25\3\25\3\25\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u00e9\n\26\3\27\3\27\3\27\3\27\5\27\u00ef\n\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\5\30\u00f6\n\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\5\31\u00fd\n\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\7\32\u0105\n\32\f\32\16\32\u0108\13\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\7\33\u0110\n\33\f\33\16\33\u0113")
        buf.write("\13\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u011b\n\34\f")
        buf.write("\34\16\34\u011e\13\34\3\35\3\35\3\35\3\35\3\35\3\35\7")
        buf.write("\35\u0126\n\35\f\35\16\35\u0129\13\35\3\36\3\36\3\36\5")
        buf.write("\36\u012e\n\36\3\37\3\37\3\37\5\37\u0133\n\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \7 \u013d\n \f \16 \u0140\13 \3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\5!\u014a\n!\3!\3!\3!\3!\7!\u0150\n!\f")
        buf.write("!\16!\u0153\13!\3\"\3\"\3\"\3\"\5\"\u0159\n\"\3\"\3\"")
        buf.write("\5\"\u015d\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\5#\u016e\n#\3$\3$\3$\3$\3$\5$\u0175\n$\3%\3%\3")
        buf.write("%\3%\3%\3&\3&\3&\3&\5&\u0180\n&\3\'\3\'\5\'\u0184\n\'")
        buf.write("\3(\3(\3(\3(\5(\u018a\n(\3)\5)\u018d\n)\3)\3)\3)\3)\3")
        buf.write("*\5*\u0194\n*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\5+\u01a2")
        buf.write("\n+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01b3")
        buf.write("\n-\3.\3.\3.\3.\3.\3.\3/\3/\3/\5/\u01be\n/\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\5\64\u01d8\n\64\3\64\3\64\3\64\3\64\2\b\62\64\668>@\65")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdf\2\13\3\2\6\t\6\2\13\f")
        buf.write("\16\16\31\31##\4\2\n\n##\3\2,/\3\2*+\3\2\60\61\3\2$%\3")
        buf.write("\2&)\3\2!\"\2\u01e7\2h\3\2\2\2\4o\3\2\2\2\6q\3\2\2\2\b")
        buf.write("\177\3\2\2\2\n\u0084\3\2\2\2\f\u0086\3\2\2\2\16\u008b")
        buf.write("\3\2\2\2\20\u0095\3\2\2\2\22\u00a1\3\2\2\2\24\u00a8\3")
        buf.write("\2\2\2\26\u00aa\3\2\2\2\30\u00ac\3\2\2\2\32\u00b8\3\2")
        buf.write("\2\2\34\u00ba\3\2\2\2\36\u00c1\3\2\2\2 \u00c7\3\2\2\2")
        buf.write("\"\u00c9\3\2\2\2$\u00d5\3\2\2\2&\u00dc\3\2\2\2(\u00e0")
        buf.write("\3\2\2\2*\u00e8\3\2\2\2,\u00ee\3\2\2\2.\u00f5\3\2\2\2")
        buf.write("\60\u00fc\3\2\2\2\62\u00fe\3\2\2\2\64\u0109\3\2\2\2\66")
        buf.write("\u0114\3\2\2\28\u011f\3\2\2\2:\u012d\3\2\2\2<\u0132\3")
        buf.write("\2\2\2>\u0134\3\2\2\2@\u0141\3\2\2\2B\u015c\3\2\2\2D\u016d")
        buf.write("\3\2\2\2F\u0174\3\2\2\2H\u0176\3\2\2\2J\u017f\3\2\2\2")
        buf.write("L\u0183\3\2\2\2N\u0189\3\2\2\2P\u018c\3\2\2\2R\u0193\3")
        buf.write("\2\2\2T\u01a1\3\2\2\2V\u01a3\3\2\2\2X\u01b2\3\2\2\2Z\u01b4")
        buf.write("\3\2\2\2\\\u01bd\3\2\2\2^\u01bf\3\2\2\2`\u01c8\3\2\2\2")
        buf.write("b\u01cb\3\2\2\2d\u01ce\3\2\2\2f\u01d2\3\2\2\2hi\5\4\3")
        buf.write("\2ij\7\2\2\3j\3\3\2\2\2kl\5\6\4\2lm\5\4\3\2mp\3\2\2\2")
        buf.write("np\5\6\4\2ok\3\2\2\2on\3\2\2\2p\5\3\2\2\2qr\7\17\2\2r")
        buf.write("u\7#\2\2st\7\26\2\2tv\7#\2\2us\3\2\2\2uv\3\2\2\2vw\3\2")
        buf.write("\2\2wx\7\67\2\2xy\5\b\5\2yz\78\2\2z\7\3\2\2\2{|\5\n\6")
        buf.write("\2|}\5\b\5\2}\u0080\3\2\2\2~\u0080\3\2\2\2\177{\3\2\2")
        buf.write("\2\177~\3\2\2\2\u0080\t\3\2\2\2\u0081\u0085\5\30\r\2\u0082")
        buf.write("\u0085\5\"\22\2\u0083\u0085\5\f\7\2\u0084\u0081\3\2\2")
        buf.write("\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085\13\3")
        buf.write("\2\2\2\u0086\u0087\5\32\16\2\u0087\u0088\5\16\b\2\u0088")
        buf.write("\u0089\5\20\t\2\u0089\u008a\7;\2\2\u008a\r\3\2\2\2\u008b")
        buf.write("\u008c\5\34\17\2\u008c\u008d\7\65\2\2\u008d\u008e\7\7")
        buf.write("\2\2\u008e\u008f\7\66\2\2\u008f\17\3\2\2\2\u0090\u0091")
        buf.write("\5\22\n\2\u0091\u0092\7>\2\2\u0092\u0093\5\20\t\2\u0093")
        buf.write("\u0096\3\2\2\2\u0094\u0096\5\22\n\2\u0095\u0090\3\2\2")
        buf.write("\2\u0095\u0094\3\2\2\2\u0096\21\3\2\2\2\u0097\u0098\7")
        buf.write("#\2\2\u0098\u0099\7\3\2\2\u0099\u009a\7\67\2\2\u009a\u009b")
        buf.write("\5\24\13\2\u009b\u009c\78\2\2\u009c\u00a2\3\2\2\2\u009d")
        buf.write("\u00a2\7#\2\2\u009e\u009f\7#\2\2\u009f\u00a0\7\3\2\2\u00a0")
        buf.write("\u00a2\5.\30\2\u00a1\u0097\3\2\2\2\u00a1\u009d\3\2\2\2")
        buf.write("\u00a1\u009e\3\2\2\2\u00a2\23\3\2\2\2\u00a3\u00a4\5\26")
        buf.write("\f\2\u00a4\u00a5\7>\2\2\u00a5\u00a6\5\24\13\2\u00a6\u00a9")
        buf.write("\3\2\2\2\u00a7\u00a9\5\26\f\2\u00a8\u00a3\3\2\2\2\u00a8")
        buf.write("\u00a7\3\2\2\2\u00a9\25\3\2\2\2\u00aa\u00ab\t\2\2\2\u00ab")
        buf.write("\27\3\2\2\2\u00ac\u00ad\5\32\16\2\u00ad\u00ae\5\34\17")
        buf.write("\2\u00ae\u00af\5\36\20\2\u00af\u00b0\7;\2\2\u00b0\31\3")
        buf.write("\2\2\2\u00b1\u00b9\7\20\2\2\u00b2\u00b9\7\21\2\2\u00b3")
        buf.write("\u00b4\7\20\2\2\u00b4\u00b9\7\21\2\2\u00b5\u00b6\7\21")
        buf.write("\2\2\u00b6\u00b9\7\20\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00b1")
        buf.write("\3\2\2\2\u00b8\u00b2\3\2\2\2\u00b8\u00b3\3\2\2\2\u00b8")
        buf.write("\u00b5\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\33\3\2\2\2\u00ba")
        buf.write("\u00bb\t\3\2\2\u00bb\35\3\2\2\2\u00bc\u00bd\5 \21\2\u00bd")
        buf.write("\u00be\7>\2\2\u00be\u00bf\5\36\20\2\u00bf\u00c2\3\2\2")
        buf.write("\2\u00c0\u00c2\5 \21\2\u00c1\u00bc\3\2\2\2\u00c1\u00c0")
        buf.write("\3\2\2\2\u00c2\37\3\2\2\2\u00c3\u00c4\7#\2\2\u00c4\u00c5")
        buf.write("\7\3\2\2\u00c5\u00c8\5.\30\2\u00c6\u00c8\7#\2\2\u00c7")
        buf.write("\u00c3\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8!\3\2\2\2\u00c9")
        buf.write("\u00ca\5$\23\2\u00ca\u00cb\5,\27\2\u00cb\u00cc\t\4\2\2")
        buf.write("\u00cc\u00ce\79\2\2\u00cd\u00cf\5&\24\2\u00ce\u00cd\3")
        buf.write("\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1")
        buf.write("\7:\2\2\u00d1\u00d2\5H%\2\u00d2#\3\2\2\2\u00d3\u00d6\7")
        buf.write("\21\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5")
        buf.write("\u00d4\3\2\2\2\u00d6%\3\2\2\2\u00d7\u00d8\5(\25\2\u00d8")
        buf.write("\u00d9\7;\2\2\u00d9\u00da\5&\24\2\u00da\u00dd\3\2\2\2")
        buf.write("\u00db\u00dd\5(\25\2\u00dc\u00d7\3\2\2\2\u00dc\u00db\3")
        buf.write("\2\2\2\u00dd\'\3\2\2\2\u00de\u00e1\5\34\17\2\u00df\u00e1")
        buf.write("\5\16\b\2\u00e0\u00de\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1")
        buf.write("\u00e2\3\2\2\2\u00e2\u00e3\5*\26\2\u00e3)\3\2\2\2\u00e4")
        buf.write("\u00e5\7#\2\2\u00e5\u00e6\7>\2\2\u00e6\u00e9\5*\26\2\u00e7")
        buf.write("\u00e9\7#\2\2\u00e8\u00e4\3\2\2\2\u00e8\u00e7\3\2\2\2")
        buf.write("\u00e9+\3\2\2\2\u00ea\u00ef\5\34\17\2\u00eb\u00ef\5\16")
        buf.write("\b\2\u00ec\u00ef\7\r\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00ea")
        buf.write("\3\2\2\2\u00ee\u00eb\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee")
        buf.write("\u00ed\3\2\2\2\u00ef-\3\2\2\2\u00f0\u00f1\5\60\31\2\u00f1")
        buf.write("\u00f2\t\5\2\2\u00f2\u00f3\5\60\31\2\u00f3\u00f6\3\2\2")
        buf.write("\2\u00f4\u00f6\5\60\31\2\u00f5\u00f0\3\2\2\2\u00f5\u00f4")
        buf.write("\3\2\2\2\u00f6/\3\2\2\2\u00f7\u00f8\5\62\32\2\u00f8\u00f9")
        buf.write("\t\6\2\2\u00f9\u00fa\5\62\32\2\u00fa\u00fd\3\2\2\2\u00fb")
        buf.write("\u00fd\5\62\32\2\u00fc\u00f7\3\2\2\2\u00fc\u00fb\3\2\2")
        buf.write("\2\u00fd\61\3\2\2\2\u00fe\u00ff\b\32\1\2\u00ff\u0100\5")
        buf.write("\64\33\2\u0100\u0106\3\2\2\2\u0101\u0102\f\4\2\2\u0102")
        buf.write("\u0103\t\7\2\2\u0103\u0105\5\64\33\2\u0104\u0101\3\2\2")
        buf.write("\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107")
        buf.write("\3\2\2\2\u0107\63\3\2\2\2\u0108\u0106\3\2\2\2\u0109\u010a")
        buf.write("\b\33\1\2\u010a\u010b\5\66\34\2\u010b\u0111\3\2\2\2\u010c")
        buf.write("\u010d\f\4\2\2\u010d\u010e\t\b\2\2\u010e\u0110\5\66\34")
        buf.write("\2\u010f\u010c\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u010f")
        buf.write("\3\2\2\2\u0111\u0112\3\2\2\2\u0112\65\3\2\2\2\u0113\u0111")
        buf.write("\3\2\2\2\u0114\u0115\b\34\1\2\u0115\u0116\58\35\2\u0116")
        buf.write("\u011c\3\2\2\2\u0117\u0118\f\4\2\2\u0118\u0119\t\t\2\2")
        buf.write("\u0119\u011b\58\35\2\u011a\u0117\3\2\2\2\u011b\u011e\3")
        buf.write("\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\67")
        buf.write("\3\2\2\2\u011e\u011c\3\2\2\2\u011f\u0120\b\35\1\2\u0120")
        buf.write("\u0121\5:\36\2\u0121\u0127\3\2\2\2\u0122\u0123\f\4\2\2")
        buf.write("\u0123\u0124\7\63\2\2\u0124\u0126\5:\36\2\u0125\u0122")
        buf.write("\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2\2\u0127")
        buf.write("\u0128\3\2\2\2\u01289\3\2\2\2\u0129\u0127\3\2\2\2\u012a")
        buf.write("\u012b\7\62\2\2\u012b\u012e\5:\36\2\u012c\u012e\5<\37")
        buf.write("\2\u012d\u012a\3\2\2\2\u012d\u012c\3\2\2\2\u012e;\3\2")
        buf.write("\2\2\u012f\u0130\t\b\2\2\u0130\u0133\5> \2\u0131\u0133")
        buf.write("\5> \2\u0132\u012f\3\2\2\2\u0132\u0131\3\2\2\2\u0133=")
        buf.write("\3\2\2\2\u0134\u0135\b \1\2\u0135\u0136\5@!\2\u0136\u013e")
        buf.write("\3\2\2\2\u0137\u0138\f\4\2\2\u0138\u0139\7\65\2\2\u0139")
        buf.write("\u013a\5.\30\2\u013a\u013b\7\66\2\2\u013b\u013d\3\2\2")
        buf.write("\2\u013c\u0137\3\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c")
        buf.write("\3\2\2\2\u013e\u013f\3\2\2\2\u013f?\3\2\2\2\u0140\u013e")
        buf.write("\3\2\2\2\u0141\u0142\b!\1\2\u0142\u0143\5B\"\2\u0143\u0151")
        buf.write("\3\2\2\2\u0144\u0145\f\5\2\2\u0145\u0146\7=\2\2\u0146")
        buf.write("\u0147\7#\2\2\u0147\u0149\79\2\2\u0148\u014a\5F$\2\u0149")
        buf.write("\u0148\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b\3\2\2\2")
        buf.write("\u014b\u0150\7:\2\2\u014c\u014d\f\4\2\2\u014d\u014e\7")
        buf.write("=\2\2\u014e\u0150\7#\2\2\u014f\u0144\3\2\2\2\u014f\u014c")
        buf.write("\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151")
        buf.write("\u0152\3\2\2\2\u0152A\3\2\2\2\u0153\u0151\3\2\2\2\u0154")
        buf.write("\u0155\7\30\2\2\u0155\u0156\7#\2\2\u0156\u0158\79\2\2")
        buf.write("\u0157\u0159\5F$\2\u0158\u0157\3\2\2\2\u0158\u0159\3\2")
        buf.write("\2\2\u0159\u015a\3\2\2\2\u015a\u015d\7:\2\2\u015b\u015d")
        buf.write("\5D#\2\u015c\u0154\3\2\2\2\u015c\u015b\3\2\2\2\u015dC")
        buf.write("\3\2\2\2\u015e\u016e\7#\2\2\u015f\u016e\7\7\2\2\u0160")
        buf.write("\u016e\7\b\2\2\u0161\u016e\7\6\2\2\u0162\u016e\7\t\2\2")
        buf.write("\u0163\u016e\7 \2\2\u0164\u016e\7\37\2\2\u0165\u0166\7")
        buf.write("9\2\2\u0166\u0167\5.\30\2\u0167\u0168\7:\2\2\u0168\u016e")
        buf.write("\3\2\2\2\u0169\u016a\7\67\2\2\u016a\u016b\5\24\13\2\u016b")
        buf.write("\u016c\78\2\2\u016c\u016e\3\2\2\2\u016d\u015e\3\2\2\2")
        buf.write("\u016d\u015f\3\2\2\2\u016d\u0160\3\2\2\2\u016d\u0161\3")
        buf.write("\2\2\2\u016d\u0162\3\2\2\2\u016d\u0163\3\2\2\2\u016d\u0164")
        buf.write("\3\2\2\2\u016d\u0165\3\2\2\2\u016d\u0169\3\2\2\2\u016e")
        buf.write("E\3\2\2\2\u016f\u0170\5.\30\2\u0170\u0171\7>\2\2\u0171")
        buf.write("\u0172\5F$\2\u0172\u0175\3\2\2\2\u0173\u0175\5.\30\2\u0174")
        buf.write("\u016f\3\2\2\2\u0174\u0173\3\2\2\2\u0175G\3\2\2\2\u0176")
        buf.write("\u0177\7\67\2\2\u0177\u0178\5J&\2\u0178\u0179\5N(\2\u0179")
        buf.write("\u017a\78\2\2\u017aI\3\2\2\2\u017b\u017c\5L\'\2\u017c")
        buf.write("\u017d\5J&\2\u017d\u0180\3\2\2\2\u017e\u0180\3\2\2\2\u017f")
        buf.write("\u017b\3\2\2\2\u017f\u017e\3\2\2\2\u0180K\3\2\2\2\u0181")
        buf.write("\u0184\5P)\2\u0182\u0184\5R*\2\u0183\u0181\3\2\2\2\u0183")
        buf.write("\u0182\3\2\2\2\u0184M\3\2\2\2\u0185\u0186\5T+\2\u0186")
        buf.write("\u0187\5N(\2\u0187\u018a\3\2\2\2\u0188\u018a\3\2\2\2\u0189")
        buf.write("\u0185\3\2\2\2\u0189\u0188\3\2\2\2\u018aO\3\2\2\2\u018b")
        buf.write("\u018d\7\20\2\2\u018c\u018b\3\2\2\2\u018c\u018d\3\2\2")
        buf.write("\2\u018d\u018e\3\2\2\2\u018e\u018f\5\34\17\2\u018f\u0190")
        buf.write("\5\36\20\2\u0190\u0191\7;\2\2\u0191Q\3\2\2\2\u0192\u0194")
        buf.write("\7\20\2\2\u0193\u0192\3\2\2\2\u0193\u0194\3\2\2\2\u0194")
        buf.write("\u0195\3\2\2\2\u0195\u0196\5\16\b\2\u0196\u0197\5\20\t")
        buf.write("\2\u0197\u0198\7;\2\2\u0198S\3\2\2\2\u0199\u01a2\5H%\2")
        buf.write("\u019a\u01a2\5V,\2\u019b\u01a2\5Z.\2\u019c\u01a2\5^\60")
        buf.write("\2\u019d\u01a2\5`\61\2\u019e\u01a2\5b\62\2\u019f\u01a2")
        buf.write("\5d\63\2\u01a0\u01a2\5f\64\2\u01a1\u0199\3\2\2\2\u01a1")
        buf.write("\u019a\3\2\2\2\u01a1\u019b\3\2\2\2\u01a1\u019c\3\2\2\2")
        buf.write("\u01a1\u019d\3\2\2\2\u01a1\u019e\3\2\2\2\u01a1\u019f\3")
        buf.write("\2\2\2\u01a1\u01a0\3\2\2\2\u01a2U\3\2\2\2\u01a3\u01a4")
        buf.write("\5X-\2\u01a4\u01a5\7\64\2\2\u01a5\u01a6\5.\30\2\u01a6")
        buf.write("\u01a7\7;\2\2\u01a7W\3\2\2\2\u01a8\u01b3\7#\2\2\u01a9")
        buf.write("\u01aa\5.\30\2\u01aa\u01ab\7=\2\2\u01ab\u01ac\7#\2\2\u01ac")
        buf.write("\u01b3\3\2\2\2\u01ad\u01ae\5.\30\2\u01ae\u01af\7\65\2")
        buf.write("\2\u01af\u01b0\5.\30\2\u01b0\u01b1\7\66\2\2\u01b1\u01b3")
        buf.write("\3\2\2\2\u01b2\u01a8\3\2\2\2\u01b2\u01a9\3\2\2\2\u01b2")
        buf.write("\u01ad\3\2\2\2\u01b3Y\3\2\2\2\u01b4\u01b5\7\27\2\2\u01b5")
        buf.write("\u01b6\5.\30\2\u01b6\u01b7\7\32\2\2\u01b7\u01b8\5T+\2")
        buf.write("\u01b8\u01b9\5\\/\2\u01b9[\3\2\2\2\u01ba\u01bb\7\25\2")
        buf.write("\2\u01bb\u01be\5T+\2\u01bc\u01be\3\2\2\2\u01bd\u01ba\3")
        buf.write("\2\2\2\u01bd\u01bc\3\2\2\2\u01be]\3\2\2\2\u01bf\u01c0")
        buf.write("\7\33\2\2\u01c0\u01c1\7#\2\2\u01c1\u01c2\7\64\2\2\u01c2")
        buf.write("\u01c3\5.\30\2\u01c3\u01c4\t\n\2\2\u01c4\u01c5\5.\30\2")
        buf.write("\u01c5\u01c6\7\24\2\2\u01c6\u01c7\5T+\2\u01c7_\3\2\2\2")
        buf.write("\u01c8\u01c9\7\22\2\2\u01c9\u01ca\7;\2\2\u01caa\3\2\2")
        buf.write("\2\u01cb\u01cc\7\23\2\2\u01cc\u01cd\7;\2\2\u01cdc\3\2")
        buf.write("\2\2\u01ce\u01cf\7\34\2\2\u01cf\u01d0\5.\30\2\u01d0\u01d1")
        buf.write("\7;\2\2\u01d1e\3\2\2\2\u01d2\u01d3\5.\30\2\u01d3\u01d4")
        buf.write("\7=\2\2\u01d4\u01d5\7#\2\2\u01d5\u01d7\79\2\2\u01d6\u01d8")
        buf.write("\5F$\2\u01d7\u01d6\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9")
        buf.write("\3\2\2\2\u01d9\u01da\7:\2\2\u01da\u01db\7;\2\2\u01dbg")
        buf.write("\3\2\2\2+ou\177\u0084\u0095\u00a1\u00a8\u00b8\u00c1\u00c7")
        buf.write("\u00ce\u00d5\u00dc\u00e0\u00e8\u00ee\u00f5\u00fc\u0106")
        buf.write("\u0111\u011c\u0127\u012d\u0132\u013e\u0149\u014f\u0151")
        buf.write("\u0158\u015c\u016d\u0174\u017f\u0183\u0189\u018c\u0193")
        buf.write("\u01a1\u01b2\u01bd\u01d7")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'main'", "'int'", 
                     "'float'", "'void'", "'boolean'", "'class'", "'final'", 
                     "'static'", "'break'", "'continue'", "'do'", "'else'", 
                     "'extends'", "'if'", "'new'", "'string'", "'then'", 
                     "'for'", "'return'", "'true'", "'false'", "'nil'", 
                     "'this'", "'to'", "'downto'", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", 
                     "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", 
                     "':='", "'['", "']'", "'{'", "'}'", "'('", "')'", "';'", 
                     "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "COMMENT", "LINE_COMMENT", 
                      "STRINGMT", "INTMT", "FLOATMT", "BOOLMT", "MAIN_LIT", 
                      "INT_LIT", "FLOAT_LIT", "VOID_LIT", "BOOL_LIT", "CLASS_LIT", 
                      "FINAL_LIT", "STATIC_LIT", "BREAK_LIT", "CONT_LIT", 
                      "DO_LIT", "ELSE_LIT", "EXTEND_LIT", "IF_LIT", "NEW_LIT", 
                      "STRING_LIT", "THEN_LIT", "FOR_LIT", "RETURN_LIT", 
                      "TRUE_LIT", "FALSE_LIT", "NIL_LIT", "THIS_LIT", "TO_LIT", 
                      "DOWNTO_LIT", "ID", "ADD_OP", "SUB_OP", "MUL_OP", 
                      "FLOAT_DIV_OP", "INT_DIV_OP", "MOD_OP", "NEQUA_OP", 
                      "ISEQUA_OP", "LESS_OP", "GREAT_OP", "LEQUA_OP", "GEQUA_OP", 
                      "OR_OP", "AND_OP", "NOT_OP", "CONCAT_OP", "ASSIGN_OP", 
                      "LSB", "RSB", "LCB", "RCB", "LB", "RB", "SEMI", "COLON", 
                      "DOT", "COMMA", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_decl_lst = 1
    RULE_class_decl = 2
    RULE_decl_lst = 3
    RULE_vm_decl = 4
    RULE_array_decl = 5
    RULE_array_type = 6
    RULE_array_lst = 7
    RULE_array_assign = 8
    RULE_array_value = 9
    RULE_array_val = 10
    RULE_var_decl = 11
    RULE_var_decl_pre = 12
    RULE_vdecl_type = 13
    RULE_var_lst = 14
    RULE_var_assign = 15
    RULE_method_decl = 16
    RULE_method_decl_pre = 17
    RULE_para_lst = 18
    RULE_para_decl = 19
    RULE_id_lst = 20
    RULE_mdecl_type = 21
    RULE_expr = 22
    RULE_expr1 = 23
    RULE_expr2 = 24
    RULE_expr3 = 25
    RULE_expr4 = 26
    RULE_expr5 = 27
    RULE_expr6 = 28
    RULE_expr7 = 29
    RULE_expr8 = 30
    RULE_expr9 = 31
    RULE_expr10 = 32
    RULE_expr11 = 33
    RULE_expr_lst = 34
    RULE_block_statement = 35
    RULE_block_decl_lst = 36
    RULE_block_decl = 37
    RULE_statement_lst = 38
    RULE_var_decl_2 = 39
    RULE_array_decl_2 = 40
    RULE_statement = 41
    RULE_assign_statement = 42
    RULE_var_name = 43
    RULE_if_statement = 44
    RULE_else_state = 45
    RULE_for_statement = 46
    RULE_break_statement = 47
    RULE_continue_statement = 48
    RULE_return_statement = 49
    RULE_methodcall_statement = 50

    ruleNames =  [ "program", "class_decl_lst", "class_decl", "decl_lst", 
                   "vm_decl", "array_decl", "array_type", "array_lst", "array_assign", 
                   "array_value", "array_val", "var_decl", "var_decl_pre", 
                   "vdecl_type", "var_lst", "var_assign", "method_decl", 
                   "method_decl_pre", "para_lst", "para_decl", "id_lst", 
                   "mdecl_type", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr8", "expr9", "expr10", 
                   "expr11", "expr_lst", "block_statement", "block_decl_lst", 
                   "block_decl", "statement_lst", "var_decl_2", "array_decl_2", 
                   "statement", "assign_statement", "var_name", "if_statement", 
                   "else_state", "for_statement", "break_statement", "continue_statement", 
                   "return_statement", "methodcall_statement" ]

    EOF = Token.EOF
    T__0=1
    COMMENT=2
    LINE_COMMENT=3
    STRINGMT=4
    INTMT=5
    FLOATMT=6
    BOOLMT=7
    MAIN_LIT=8
    INT_LIT=9
    FLOAT_LIT=10
    VOID_LIT=11
    BOOL_LIT=12
    CLASS_LIT=13
    FINAL_LIT=14
    STATIC_LIT=15
    BREAK_LIT=16
    CONT_LIT=17
    DO_LIT=18
    ELSE_LIT=19
    EXTEND_LIT=20
    IF_LIT=21
    NEW_LIT=22
    STRING_LIT=23
    THEN_LIT=24
    FOR_LIT=25
    RETURN_LIT=26
    TRUE_LIT=27
    FALSE_LIT=28
    NIL_LIT=29
    THIS_LIT=30
    TO_LIT=31
    DOWNTO_LIT=32
    ID=33
    ADD_OP=34
    SUB_OP=35
    MUL_OP=36
    FLOAT_DIV_OP=37
    INT_DIV_OP=38
    MOD_OP=39
    NEQUA_OP=40
    ISEQUA_OP=41
    LESS_OP=42
    GREAT_OP=43
    LEQUA_OP=44
    GEQUA_OP=45
    OR_OP=46
    AND_OP=47
    NOT_OP=48
    CONCAT_OP=49
    ASSIGN_OP=50
    LSB=51
    RSB=52
    LCB=53
    RCB=54
    LB=55
    RB=56
    SEMI=57
    COLON=58
    DOT=59
    COMMA=60
    WS=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_decl_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Class_decl_lstContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.class_decl_lst()
            self.state = 103
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_decl_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Class_declContext,0)


        def class_decl_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Class_decl_lstContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_decl_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl_lst" ):
                return visitor.visitClass_decl_lst(self)
            else:
                return visitor.visitChildren(self)




    def class_decl_lst(self):

        localctx = BKOOLParser.Class_decl_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl_lst)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.class_decl()
                self.state = 106
                self.class_decl_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.class_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS_LIT(self):
            return self.getToken(BKOOLParser.CLASS_LIT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def decl_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_lstContext,0)


        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def EXTEND_LIT(self):
            return self.getToken(BKOOLParser.EXTEND_LIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = BKOOLParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(BKOOLParser.CLASS_LIT)
            self.state = 112
            self.match(BKOOLParser.ID)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTEND_LIT:
                self.state = 113
                self.match(BKOOLParser.EXTEND_LIT)
                self.state = 114
                self.match(BKOOLParser.ID)


            self.state = 117
            self.match(BKOOLParser.LCB)
            self.state = 118
            self.decl_lst()
            self.state = 119
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vm_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Vm_declContext,0)


        def decl_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_lstContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_lst" ):
                return visitor.visitDecl_lst(self)
            else:
                return visitor.visitChildren(self)




    def decl_lst(self):

        localctx = BKOOLParser.Decl_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl_lst)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.MAIN_LIT, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.VOID_LIT, BKOOLParser.BOOL_LIT, BKOOLParser.FINAL_LIT, BKOOLParser.STATIC_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.vm_decl()
                self.state = 122
                self.decl_lst()
                pass
            elif token in [BKOOLParser.RCB]:
                self.enterOuterAlt(localctx, 2)

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


    class Vm_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Var_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Method_declContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Array_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_vm_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVm_decl" ):
                return visitor.visitVm_decl(self)
            else:
                return visitor.visitChildren(self)




    def vm_decl(self):

        localctx = BKOOLParser.Vm_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vm_decl)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.method_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.array_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_pre(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_preContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def array_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Array_lstContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = BKOOLParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.var_decl_pre()
            self.state = 133
            self.array_type()
            self.state = 134
            self.array_lst()
            self.state = 135
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vdecl_type(self):
            return self.getTypedRuleContext(BKOOLParser.Vdecl_typeContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTMT(self):
            return self.getToken(BKOOLParser.INTMT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.vdecl_type()
            self.state = 138
            self.match(BKOOLParser.LSB)
            self.state = 139
            self.match(BKOOLParser.INTMT)
            self.state = 140
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_assign(self):
            return self.getTypedRuleContext(BKOOLParser.Array_assignContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def array_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Array_lstContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lst" ):
                return visitor.visitArray_lst(self)
            else:
                return visitor.visitChildren(self)




    def array_lst(self):

        localctx = BKOOLParser.Array_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_lst)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.array_assign()
                self.state = 143
                self.match(BKOOLParser.COMMA)
                self.state = 144
                self.array_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.array_assign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def array_value(self):
            return self.getTypedRuleContext(BKOOLParser.Array_valueContext,0)


        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_assign" ):
                return visitor.visitArray_assign(self)
            else:
                return visitor.visitChildren(self)




    def array_assign(self):

        localctx = BKOOLParser.Array_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_assign)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(BKOOLParser.ID)
                self.state = 150
                self.match(BKOOLParser.T__0)
                self.state = 151
                self.match(BKOOLParser.LCB)
                self.state = 152
                self.array_value()
                self.state = 153
                self.match(BKOOLParser.RCB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.match(BKOOLParser.ID)
                self.state = 157
                self.match(BKOOLParser.T__0)
                self.state = 158
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_val(self):
            return self.getTypedRuleContext(BKOOLParser.Array_valContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def array_value(self):
            return self.getTypedRuleContext(BKOOLParser.Array_valueContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value" ):
                return visitor.visitArray_value(self)
            else:
                return visitor.visitChildren(self)




    def array_value(self):

        localctx = BKOOLParser.Array_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_value)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.array_val()
                self.state = 162
                self.match(BKOOLParser.COMMA)
                self.state = 163
                self.array_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.array_val()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLMT(self):
            return self.getToken(BKOOLParser.BOOLMT, 0)

        def STRINGMT(self):
            return self.getToken(BKOOLParser.STRINGMT, 0)

        def INTMT(self):
            return self.getToken(BKOOLParser.INTMT, 0)

        def FLOATMT(self):
            return self.getToken(BKOOLParser.FLOATMT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_val" ):
                return visitor.visitArray_val(self)
            else:
                return visitor.visitChildren(self)




    def array_val(self):

        localctx = BKOOLParser.Array_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.STRINGMT) | (1 << BKOOLParser.INTMT) | (1 << BKOOLParser.FLOATMT) | (1 << BKOOLParser.BOOLMT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_pre(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_preContext,0)


        def vdecl_type(self):
            return self.getTypedRuleContext(BKOOLParser.Vdecl_typeContext,0)


        def var_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Var_lstContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = BKOOLParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.var_decl_pre()
            self.state = 171
            self.vdecl_type()
            self.state = 172
            self.var_lst()
            self.state = 173
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_preContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL_LIT(self):
            return self.getToken(BKOOLParser.FINAL_LIT, 0)

        def STATIC_LIT(self):
            return self.getToken(BKOOLParser.STATIC_LIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl_pre

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_pre" ):
                return visitor.visitVar_decl_pre(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_pre(self):

        localctx = BKOOLParser.Var_decl_preContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_var_decl_pre)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(BKOOLParser.FINAL_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(BKOOLParser.STATIC_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.match(BKOOLParser.FINAL_LIT)
                self.state = 178
                self.match(BKOOLParser.STATIC_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 179
                self.match(BKOOLParser.STATIC_LIT)
                self.state = 180
                self.match(BKOOLParser.FINAL_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vdecl_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(BKOOLParser.BOOL_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vdecl_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVdecl_type" ):
                return visitor.visitVdecl_type(self)
            else:
                return visitor.visitChildren(self)




    def vdecl_type(self):

        localctx = BKOOLParser.Vdecl_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_vdecl_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.BOOL_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_assign(self):
            return self.getTypedRuleContext(BKOOLParser.Var_assignContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def var_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Var_lstContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_lst" ):
                return visitor.visitVar_lst(self)
            else:
                return visitor.visitChildren(self)




    def var_lst(self):

        localctx = BKOOLParser.Var_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_var_lst)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.var_assign()
                self.state = 187
                self.match(BKOOLParser.COMMA)
                self.state = 188
                self.var_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.var_assign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_assign" ):
                return visitor.visitVar_assign(self)
            else:
                return visitor.visitChildren(self)




    def var_assign(self):

        localctx = BKOOLParser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_var_assign)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(BKOOLParser.ID)
                self.state = 194
                self.match(BKOOLParser.T__0)
                self.state = 195
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_decl_pre(self):
            return self.getTypedRuleContext(BKOOLParser.Method_decl_preContext,0)


        def mdecl_type(self):
            return self.getTypedRuleContext(BKOOLParser.Mdecl_typeContext,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def block_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Block_statementContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def MAIN_LIT(self):
            return self.getToken(BKOOLParser.MAIN_LIT, 0)

        def para_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Para_lstContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = BKOOLParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.method_decl_pre()
            self.state = 200
            self.mdecl_type()
            self.state = 201
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.MAIN_LIT or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 202
            self.match(BKOOLParser.LB)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.BOOL_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 203
                self.para_lst()


            self.state = 206
            self.match(BKOOLParser.RB)
            self.state = 207
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_decl_preContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC_LIT(self):
            return self.getToken(BKOOLParser.STATIC_LIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method_decl_pre

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl_pre" ):
                return visitor.visitMethod_decl_pre(self)
            else:
                return visitor.visitChildren(self)




    def method_decl_pre(self):

        localctx = BKOOLParser.Method_decl_preContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_method_decl_pre)
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(BKOOLParser.STATIC_LIT)
                pass
            elif token in [BKOOLParser.MAIN_LIT, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.VOID_LIT, BKOOLParser.BOOL_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)

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


    class Para_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Para_declContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def para_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Para_lstContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_para_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_lst" ):
                return visitor.visitPara_lst(self)
            else:
                return visitor.visitChildren(self)




    def para_lst(self):

        localctx = BKOOLParser.Para_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_para_lst)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.para_decl()
                self.state = 214
                self.match(BKOOLParser.SEMI)
                self.state = 215
                self.para_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.para_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Id_lstContext,0)


        def vdecl_type(self):
            return self.getTypedRuleContext(BKOOLParser.Vdecl_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_para_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_decl" ):
                return visitor.visitPara_decl(self)
            else:
                return visitor.visitChildren(self)




    def para_decl(self):

        localctx = BKOOLParser.Para_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_para_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 220
                self.vdecl_type()
                pass

            elif la_ == 2:
                self.state = 221
                self.array_type()
                pass


            self.state = 224
            self.id_lst()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def id_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Id_lstContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_id_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_lst" ):
                return visitor.visitId_lst(self)
            else:
                return visitor.visitChildren(self)




    def id_lst(self):

        localctx = BKOOLParser.Id_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_id_lst)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(BKOOLParser.ID)
                self.state = 227
                self.match(BKOOLParser.COMMA)
                self.state = 228
                self.id_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mdecl_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vdecl_type(self):
            return self.getTypedRuleContext(BKOOLParser.Vdecl_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def VOID_LIT(self):
            return self.getToken(BKOOLParser.VOID_LIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mdecl_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMdecl_type" ):
                return visitor.visitMdecl_type(self)
            else:
                return visitor.visitChildren(self)




    def mdecl_type(self):

        localctx = BKOOLParser.Mdecl_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_mdecl_type)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.vdecl_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.array_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.match(BKOOLParser.VOID_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass


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

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr1Context,i)


        def GREAT_OP(self):
            return self.getToken(BKOOLParser.GREAT_OP, 0)

        def LESS_OP(self):
            return self.getToken(BKOOLParser.LESS_OP, 0)

        def GEQUA_OP(self):
            return self.getToken(BKOOLParser.GEQUA_OP, 0)

        def LEQUA_OP(self):
            return self.getToken(BKOOLParser.LEQUA_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.expr1()
                self.state = 239
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS_OP) | (1 << BKOOLParser.GREAT_OP) | (1 << BKOOLParser.LEQUA_OP) | (1 << BKOOLParser.GEQUA_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 240
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr2Context,i)


        def ISEQUA_OP(self):
            return self.getToken(BKOOLParser.ISEQUA_OP, 0)

        def NEQUA_OP(self):
            return self.getToken(BKOOLParser.NEQUA_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.expr2(0)
                self.state = 246
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NEQUA_OP or _la==BKOOLParser.ISEQUA_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 247
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def AND_OP(self):
            return self.getToken(BKOOLParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(BKOOLParser.OR_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 255
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 256
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR_OP or _la==BKOOLParser.AND_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 257
                    self.expr3(0) 
                self.state = 262
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def ADD_OP(self):
            return self.getToken(BKOOLParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(BKOOLParser.SUB_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 271
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 266
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 267
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD_OP or _la==BKOOLParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 268
                    self.expr4(0) 
                self.state = 273
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def MUL_OP(self):
            return self.getToken(BKOOLParser.MUL_OP, 0)

        def INT_DIV_OP(self):
            return self.getToken(BKOOLParser.INT_DIV_OP, 0)

        def FLOAT_DIV_OP(self):
            return self.getToken(BKOOLParser.FLOAT_DIV_OP, 0)

        def MOD_OP(self):
            return self.getToken(BKOOLParser.MOD_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 277
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 278
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL_OP) | (1 << BKOOLParser.FLOAT_DIV_OP) | (1 << BKOOLParser.INT_DIV_OP) | (1 << BKOOLParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 279
                    self.expr5(0) 
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def CONCAT_OP(self):
            return self.getToken(BKOOLParser.CONCAT_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 288
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 289
                    self.match(BKOOLParser.CONCAT_OP)
                    self.state = 290
                    self.expr6() 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT_OP(self):
            return self.getToken(BKOOLParser.NOT_OP, 0)

        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = BKOOLParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr6)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(BKOOLParser.NOT_OP)
                self.state = 297
                self.expr6()
                pass
            elif token in [BKOOLParser.STRINGMT, BKOOLParser.INTMT, BKOOLParser.FLOATMT, BKOOLParser.BOOLMT, BKOOLParser.NEW_LIT, BKOOLParser.NIL_LIT, BKOOLParser.THIS_LIT, BKOOLParser.ID, BKOOLParser.ADD_OP, BKOOLParser.SUB_OP, BKOOLParser.LCB, BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.expr7()
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def ADD_OP(self):
            return self.getToken(BKOOLParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(BKOOLParser.SUB_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = BKOOLParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr7)
        self._la = 0 # Token type
        try:
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD_OP, BKOOLParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD_OP or _la==BKOOLParser.SUB_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 302
                self.expr8(0)
                pass
            elif token in [BKOOLParser.STRINGMT, BKOOLParser.INTMT, BKOOLParser.FLOATMT, BKOOLParser.BOOLMT, BKOOLParser.NEW_LIT, BKOOLParser.NIL_LIT, BKOOLParser.THIS_LIT, BKOOLParser.ID, BKOOLParser.LCB, BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.expr8(0)
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


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.expr9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 316
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 309
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 310
                    self.match(BKOOLParser.LSB)
                    self.state = 311
                    self.expr()
                    self.state = 312
                    self.match(BKOOLParser.RSB) 
                self.state = 318
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr10(self):
            return self.getTypedRuleContext(BKOOLParser.Expr10Context,0)


        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_lstContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)



    def expr9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr9, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.expr10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 335
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 333
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 322
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 323
                        self.match(BKOOLParser.DOT)
                        self.state = 324
                        self.match(BKOOLParser.ID)

                        self.state = 325
                        self.match(BKOOLParser.LB)
                        self.state = 327
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.STRINGMT) | (1 << BKOOLParser.INTMT) | (1 << BKOOLParser.FLOATMT) | (1 << BKOOLParser.BOOLMT) | (1 << BKOOLParser.NEW_LIT) | (1 << BKOOLParser.NIL_LIT) | (1 << BKOOLParser.THIS_LIT) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.ADD_OP) | (1 << BKOOLParser.SUB_OP) | (1 << BKOOLParser.NOT_OP) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.LB))) != 0):
                            self.state = 326
                            self.expr_lst()


                        self.state = 329
                        self.match(BKOOLParser.RB)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 330
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 331
                        self.match(BKOOLParser.DOT)
                        self.state = 332
                        self.match(BKOOLParser.ID)
                        pass

             
                self.state = 337
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW_LIT(self):
            return self.getToken(BKOOLParser.NEW_LIT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_lstContext,0)


        def expr11(self):
            return self.getTypedRuleContext(BKOOLParser.Expr11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = BKOOLParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(BKOOLParser.NEW_LIT)
                self.state = 339
                self.match(BKOOLParser.ID)
                self.state = 340
                self.match(BKOOLParser.LB)
                self.state = 342
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.STRINGMT) | (1 << BKOOLParser.INTMT) | (1 << BKOOLParser.FLOATMT) | (1 << BKOOLParser.BOOLMT) | (1 << BKOOLParser.NEW_LIT) | (1 << BKOOLParser.NIL_LIT) | (1 << BKOOLParser.THIS_LIT) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.ADD_OP) | (1 << BKOOLParser.SUB_OP) | (1 << BKOOLParser.NOT_OP) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.LB))) != 0):
                    self.state = 341
                    self.expr_lst()


                self.state = 344
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.STRINGMT, BKOOLParser.INTMT, BKOOLParser.FLOATMT, BKOOLParser.BOOLMT, BKOOLParser.NIL_LIT, BKOOLParser.THIS_LIT, BKOOLParser.ID, BKOOLParser.LCB, BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.expr11()
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


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INTMT(self):
            return self.getToken(BKOOLParser.INTMT, 0)

        def FLOATMT(self):
            return self.getToken(BKOOLParser.FLOATMT, 0)

        def STRINGMT(self):
            return self.getToken(BKOOLParser.STRINGMT, 0)

        def BOOLMT(self):
            return self.getToken(BKOOLParser.BOOLMT, 0)

        def THIS_LIT(self):
            return self.getToken(BKOOLParser.THIS_LIT, 0)

        def NIL_LIT(self):
            return self.getToken(BKOOLParser.NIL_LIT, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def array_value(self):
            return self.getTypedRuleContext(BKOOLParser.Array_valueContext,0)


        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = BKOOLParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr11)
        try:
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.INTMT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.match(BKOOLParser.INTMT)
                pass
            elif token in [BKOOLParser.FLOATMT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 350
                self.match(BKOOLParser.FLOATMT)
                pass
            elif token in [BKOOLParser.STRINGMT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 351
                self.match(BKOOLParser.STRINGMT)
                pass
            elif token in [BKOOLParser.BOOLMT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 352
                self.match(BKOOLParser.BOOLMT)
                pass
            elif token in [BKOOLParser.THIS_LIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 353
                self.match(BKOOLParser.THIS_LIT)
                pass
            elif token in [BKOOLParser.NIL_LIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 354
                self.match(BKOOLParser.NIL_LIT)
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 8)
                self.state = 355
                self.match(BKOOLParser.LB)
                self.state = 356
                self.expr()
                self.state = 357
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.LCB]:
                self.enterOuterAlt(localctx, 9)
                self.state = 359
                self.match(BKOOLParser.LCB)
                self.state = 360
                self.array_value()
                self.state = 361
                self.match(BKOOLParser.RCB)
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


    class Expr_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_lstContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_lst" ):
                return visitor.visitExpr_lst(self)
            else:
                return visitor.visitChildren(self)




    def expr_lst(self):

        localctx = BKOOLParser.Expr_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr_lst)
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.expr()
                self.state = 366
                self.match(BKOOLParser.COMMA)
                self.state = 367
                self.expr_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def block_decl_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Block_decl_lstContext,0)


        def statement_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Statement_lstContext,0)


        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = BKOOLParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(BKOOLParser.LCB)
            self.state = 373
            self.block_decl_lst()
            self.state = 374
            self.statement_lst()
            self.state = 375
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_decl_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Block_declContext,0)


        def block_decl_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Block_decl_lstContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_decl_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_decl_lst" ):
                return visitor.visitBlock_decl_lst(self)
            else:
                return visitor.visitChildren(self)




    def block_decl_lst(self):

        localctx = BKOOLParser.Block_decl_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_block_decl_lst)
        try:
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.block_decl()
                self.state = 378
                self.block_decl_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_2(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_2Context,0)


        def array_decl_2(self):
            return self.getTypedRuleContext(BKOOLParser.Array_decl_2Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_decl" ):
                return visitor.visitBlock_decl(self)
            else:
                return visitor.visitChildren(self)




    def block_decl(self):

        localctx = BKOOLParser.Block_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_block_decl)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.var_decl_2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.array_decl_2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def statement_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Statement_lstContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_lst" ):
                return visitor.visitStatement_lst(self)
            else:
                return visitor.visitChildren(self)




    def statement_lst(self):

        localctx = BKOOLParser.Statement_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_statement_lst)
        try:
            self.state = 391
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STRINGMT, BKOOLParser.INTMT, BKOOLParser.FLOATMT, BKOOLParser.BOOLMT, BKOOLParser.BREAK_LIT, BKOOLParser.CONT_LIT, BKOOLParser.IF_LIT, BKOOLParser.NEW_LIT, BKOOLParser.FOR_LIT, BKOOLParser.RETURN_LIT, BKOOLParser.NIL_LIT, BKOOLParser.THIS_LIT, BKOOLParser.ID, BKOOLParser.ADD_OP, BKOOLParser.SUB_OP, BKOOLParser.NOT_OP, BKOOLParser.LCB, BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.statement()
                self.state = 388
                self.statement_lst()
                pass
            elif token in [BKOOLParser.RCB]:
                self.enterOuterAlt(localctx, 2)

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


    class Var_decl_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vdecl_type(self):
            return self.getTypedRuleContext(BKOOLParser.Vdecl_typeContext,0)


        def var_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Var_lstContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL_LIT(self):
            return self.getToken(BKOOLParser.FINAL_LIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_2" ):
                return visitor.visitVar_decl_2(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_2(self):

        localctx = BKOOLParser.Var_decl_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_var_decl_2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL_LIT:
                self.state = 393
                self.match(BKOOLParser.FINAL_LIT)


            self.state = 396
            self.vdecl_type()
            self.state = 397
            self.var_lst()
            self.state = 398
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_decl_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def array_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Array_lstContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL_LIT(self):
            return self.getToken(BKOOLParser.FINAL_LIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_decl_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl_2" ):
                return visitor.visitArray_decl_2(self)
            else:
                return visitor.visitChildren(self)




    def array_decl_2(self):

        localctx = BKOOLParser.Array_decl_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_array_decl_2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL_LIT:
                self.state = 400
                self.match(BKOOLParser.FINAL_LIT)


            self.state = 403
            self.array_type()
            self.state = 404
            self.array_lst()
            self.state = 405
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Block_statementContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(BKOOLParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(BKOOLParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Return_statementContext,0)


        def methodcall_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Methodcall_statementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKOOLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_statement)
        try:
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.block_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 409
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 410
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 411
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 412
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 413
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 414
                self.methodcall_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_name(self):
            return self.getTypedRuleContext(BKOOLParser.Var_nameContext,0)


        def ASSIGN_OP(self):
            return self.getToken(BKOOLParser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = BKOOLParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.var_name()
            self.state = 418
            self.match(BKOOLParser.ASSIGN_OP)
            self.state = 419
            self.expr()
            self.state = 420
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_name" ):
                return visitor.visitVar_name(self)
            else:
                return visitor.visitChildren(self)




    def var_name(self):

        localctx = BKOOLParser.Var_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_var_name)
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.expr()
                self.state = 424
                self.match(BKOOLParser.DOT)
                self.state = 425
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 427
                self.expr()
                self.state = 428
                self.match(BKOOLParser.LSB)
                self.state = 429
                self.expr()
                self.state = 430
                self.match(BKOOLParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_LIT(self):
            return self.getToken(BKOOLParser.IF_LIT, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def THEN_LIT(self):
            return self.getToken(BKOOLParser.THEN_LIT, 0)

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def else_state(self):
            return self.getTypedRuleContext(BKOOLParser.Else_stateContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = BKOOLParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(BKOOLParser.IF_LIT)
            self.state = 435
            self.expr()
            self.state = 436
            self.match(BKOOLParser.THEN_LIT)
            self.state = 437
            self.statement()
            self.state = 438
            self.else_state()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE_LIT(self):
            return self.getToken(BKOOLParser.ELSE_LIT, 0)

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_else_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_state" ):
                return visitor.visitElse_state(self)
            else:
                return visitor.visitChildren(self)




    def else_state(self):

        localctx = BKOOLParser.Else_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_else_state)
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.match(BKOOLParser.ELSE_LIT)
                self.state = 441
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_LIT(self):
            return self.getToken(BKOOLParser.FOR_LIT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN_OP(self):
            return self.getToken(BKOOLParser.ASSIGN_OP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def DO_LIT(self):
            return self.getToken(BKOOLParser.DO_LIT, 0)

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def TO_LIT(self):
            return self.getToken(BKOOLParser.TO_LIT, 0)

        def DOWNTO_LIT(self):
            return self.getToken(BKOOLParser.DOWNTO_LIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = BKOOLParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(BKOOLParser.FOR_LIT)
            self.state = 446
            self.match(BKOOLParser.ID)
            self.state = 447
            self.match(BKOOLParser.ASSIGN_OP)
            self.state = 448
            self.expr()
            self.state = 449
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO_LIT or _la==BKOOLParser.DOWNTO_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 450
            self.expr()
            self.state = 451
            self.match(BKOOLParser.DO_LIT)
            self.state = 452
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_LIT(self):
            return self.getToken(BKOOLParser.BREAK_LIT, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = BKOOLParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(BKOOLParser.BREAK_LIT)
            self.state = 455
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONT_LIT(self):
            return self.getToken(BKOOLParser.CONT_LIT, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = BKOOLParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(BKOOLParser.CONT_LIT)
            self.state = 458
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_LIT(self):
            return self.getToken(BKOOLParser.RETURN_LIT, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = BKOOLParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(BKOOLParser.RETURN_LIT)
            self.state = 461
            self.expr()
            self.state = 462
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Methodcall_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_lstContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodcall_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodcall_statement" ):
                return visitor.visitMethodcall_statement(self)
            else:
                return visitor.visitChildren(self)




    def methodcall_statement(self):

        localctx = BKOOLParser.Methodcall_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_methodcall_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.expr()
            self.state = 465
            self.match(BKOOLParser.DOT)
            self.state = 466
            self.match(BKOOLParser.ID)
            self.state = 467
            self.match(BKOOLParser.LB)
            self.state = 469
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.STRINGMT) | (1 << BKOOLParser.INTMT) | (1 << BKOOLParser.FLOATMT) | (1 << BKOOLParser.BOOLMT) | (1 << BKOOLParser.NEW_LIT) | (1 << BKOOLParser.NIL_LIT) | (1 << BKOOLParser.THIS_LIT) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.ADD_OP) | (1 << BKOOLParser.SUB_OP) | (1 << BKOOLParser.NOT_OP) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.LB))) != 0):
                self.state = 468
                self.expr_lst()


            self.state = 471
            self.match(BKOOLParser.RB)
            self.state = 472
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[24] = self.expr2_sempred
        self._predicates[25] = self.expr3_sempred
        self._predicates[26] = self.expr4_sempred
        self._predicates[27] = self.expr5_sempred
        self._predicates[30] = self.expr8_sempred
        self._predicates[31] = self.expr9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr9_sempred(self, localctx:Expr9Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




