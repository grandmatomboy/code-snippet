import json

unicode_dict= {
    "Α":"alpha", #\u0391
    "Β":"beta", #\u0392
    "Γ":"gamma", #\u0393
    "Δ":"delta", #\u0394
    "Ε":"epsilon", #\u0395
    "Ζ":"zeta", #\u0396
    "Η":"eta", #\u0397
    "Θ":"theta", #\u0398
    "Ι":"iota", #\u0399
    "Κ":"kappa", #\u039a
    "Λ":"lambda", #\u039b
    "Μ":"mu", #\u039c
    "Ν":"nu", #\u039d
    "Ξ":"xi", #\u039e
    "Ο":"omicron", #\u039f
    "Π":"pi", #\u03a0
    "Ρ":"rho", #\u03a1
    "Σ":"sigma", #\u03a3
    "Τ":"tau", #\u03a4
    "Υ":"upsilon", #\u03a5
    "Φ":"phi", #\u036
    "Χ":"chi", #\u03a7
    "Ψ":"psi", #\u03a8
    "Ω":"omega", #\u03a9
    "α":"alpha", #\u03b1
    "β":"beta", #\u03b2
    "γ":"gamma", #\u03b3
    "δ":"delta", #\u03b4
    "ε":"epsilon", #\u03b5
    "ζ":"zeta", #\u03b6
    "η":"eta", #\u03b7
    "θ":"theta", #\u03b8
    "ι":"iota", #\u03b9
    "κ":"kappa", #\u03ba
    "λ":"lambda", #\u03bb
    "μ":"mu", #\u03bc
    "ν":"nu", #\u03bd
    "ξ":"xi", #\u03be
    "ο":"omicron", #\u03bf
    "π":"pi", #\u03c0
    "ρ":"rho", #\u03c1
    "σ":"sigma", #\u03c3
    "τ":"tau", #\u03c4
    "υ":"upsilon", #\u03c5
    "φ":"phi", #\u03c6
    "χ":"chi", #\u03c7
    "ψ":"psi", #\u03c8
    "ω":"omega", #\u03c9
    "‐": "-", #\u2010 hypen
    "–": "-", #\u2013 dash 
    "—": "-", #\u2014 dash 
    "−": "-", #\u2212
    "’": "'", #\u2019 right quotation mark
    "…": "...", #\u2026 horizontal ellipsis
    "©": "", #\u00a9
    "®": "", #\u00ae
    "¯": "-", #\u00af
    "°": "deg.", #\u00b0
    "∞": "infinity", #\u221e
    "，": ",", #\uff0c
    "À": "A", #\u00c0
    "Á": "A", #\u00c1
    "Â": "A", #\u00c2
    "Ã": "A", #\u00c3
    "Ä": "A", #\u00c4
    "Å": "A", #\u00c5
    "Æ": "AE", #\u00c6
    "Ç": "C", #\u00c7
    "È": "E", #\u00c8
    "É": "E", #\u00c9
    "Ê": "E", #\u00ca
    "Ë": "E", #\u00cb
    "Ì": "I", #\u00cc
    "Í": "I", #\u00cd
    "Î": "I", #\u00ce
    "Ï": "I", #\u00cf
    "Ð": "D", #\u00d0
    "Ñ": "N", #\u00d1
    "Ò": "O", #\u00d2
    "Ó": "O", #\u00d3
    "Ô": "O", #\u00d4
    "Õ": "O", #\u00d5
    "Ö": "O", #\u00d6
    "×": "x", #\u00d7
    "Ø": "0", #\u00d8
    "Ù": "U", #\u00d9
    "Ú": "U", #\u00da
    "Û": "U", #\u00db
    "Ü": "U", #\u00dc
    "Ý": "Y", #\u00dd
    "ß": "ss", #\u00df
    "à": "a", #\u00e0
    "á": "a", #\u00e1
    "â": "a", #\u00e2
    "ã": "a", #\u00e3
    "ä": "a", #\u00e4
    "å": "a", #\u00e5
    "æ": "ae", #\u00e6
    "ç": "c", #\u00e7
    "è": "e", #\u00e8
    "é": "e", #\u00e9
    "ê": "e", #\u00ea
    "ë": "e", #\u00eb
    "ì": "i", #\u00ec
    "í": "i", #\u00ed
    "î": "i", #\u00ee
    "ï": "i", #\u00ef
    "ð": "", #\u00f0
    "ñ": "n", #\u00f1
    "ò": "o", #\u00f2
    "ó": "o", #\u00f3
    "ô": "o", #\u00f4
    "õ": "o", #\u00f5
    "ö": "o", #\u00f6
    "÷": "//", #\u00f7
    "ø": "o", #\u00f8
    "ù": "u", #\u00f9
    "ú": "u", #\u00fa
    "û": "u", #\u00fb
    "ü": "u", #\u00fc
    "ý": "u", #\u00fd
    "þ": "", #\u00fe
    "ÿ": "y", #\u00ff
    "Ā": "A", #\u0100
    "ā": "a", #\u0101
    "Ă": "A", #\u0102
    "ă": "a", #\u0103
    "Ą": "A", #\u0104
    "ą": "a", #\u0105
    "Ć": "C", #\u0106
    "ć": "c", #\u0107
    "Ĉ": "c", #\u0108
    "ĉ": "c", #\u0109
    "Ċ": "C", #\u010a
    "ċ": "c", #\u010b
    "Č": "C", #\u010c
    "č": "c", #\u010d
    "Ď": "D", #\u010e
    "ď": "d", #\u010f
    "Đ": "D", #\u0110
    "đ": "d", #\u0111
    "Ē": "E", #\u0112
    "ē": "e", #\u0113
    "Ĕ": "E", #\u0114
    "ĕ": "e", #\u0115
    "Ė": "E", #\u0116
    "ė": "e", #\u0117
    "Ę": "E", #\u0118
    "ę": "e", #\u0119
    "Ě": "E", #\u011a
    "ě": "e", #\u011b
    "Ĝ": "G", #\u011c
    "ĝ": "g", #\u011d
    "Ğ": "G", #\u011e
    "ğ": "ğ", #\u011f
    "Ġ": "G", #\u0120
    "ġ": "g", #\u0121
    "Ģ": "G", #\u0122
    "ģ": "g", #\u0123
    "Ĥ": "H", #\u0124
    "ĥ": "h", #\u0125
    "Ħ": "H", #\u0126
    "ħ": "h", #\u0127
    "Ĩ": "I", #\u0128
    "ĩ": "i", #\u0129
    "Ī": "I", #\u012a
    "ī": "i", #\u012b
    "Ĭ": "I", #\u012c
    "ĭ": "i", #\u012d
    "Į": "I", #\u012e
    "į": "i", #\u012f
    "İ": "I", #\u0130
    "ı": "i", #\u0131
    "Ĳ": "IJ", #\u0132
    "ĳ": "ij", #\u0133
    "Ĵ": "J", #\u0134
    "ĵ": "j", #\u0135
    "Ķ": "K", #\u0136
    "ķ": "k", #\u0137
    "ĸ": "K", #\u0138
    "Ĺ": "L", #\u0139
    "ĺ": "l", #\u013a
    "Ļ": "L", #\u013b
    "ļ": "l", #\u013c
    "Ľ": "L", #\u013d
    "ľ": "l", #\u013e
    "Ŀ": "L", #\u013f
    "ŀ": "l", #\u0140
    "Ł": "L", #\u0141
    "ł": "l", #\u0142
    "Ń": "N", #\u0143
    "ń": "n", #\u0144
    "Ņ": "N", #\u0145
    "ņ": "n", #\u0146
    "Ň": "N", #\u0147
    "ň": "n", #\u0148
    "ŉ": "n", #\u0149
    "Ŋ": "N", #\u014a
    "ŋ": "n", #\u014b
    "Ō": "O", #\u014c
    "ō": "o", #\u014d
    "Ŏ": "O", #\u014e
    "ŏ": "o", #\u014f
    "Ő": "O", #\u0150
    "ő": "o", #\u0151
    "Œ": "OE", #\u0152
    "œ": "oe", #\u0153
    "Ŕ": "R", #\u0154
    "ŕ": "r", #\u0155
    "Ŗ": "R", #\u0156
    "ŗ": "r", #\u0157
    "Ř": "R", #\u0158
    "ř": "r", #\u0159
    "Ś": "S", #\u015a
    "ś": "s", #\u015b
    "Ŝ": "S", #\u015c
    "ŝ": "s", #\u015d
    "Ş": "S", #\u015e
    "ş": "s", #\u015f
    "Š": "S", #\u0160
    "š": "s", #\u0161
    "Ţ": "T", #\u0162
    "ţ": "t", #\u0163
    "Ť": "T", #\u0164
    "ť": "t", #\u0165
    "Ŧ": "T", #\u0166
    "ŧ": "t", #\u0167
    "Ũ": "U", #\u0168
    "ũ": "u", #\u0169
    "Ū": "U", #\u016a
    "ū": "u", #\u016b
    "Ŭ": "U", #\u016c
    "ŭ": "u", #\u016d
    "Ů": "U", #\u016e
    "ů": "u", #\u016f
    "Ű": "U", #\u0170
    "ű": "u", #\u0171
    "Ų": "U", #\u0172
    "ų": "u", #\u0173
    "Ŵ": "W", #\u0174
    "ŵ": "w", #\u0175
    "Ŷ": "Y", #\u0176
    "ŷ": "y", #\u0177
    "Ÿ": "Y", #\u0178
    "Ź": "Z", #\u0179
    "ź": "z", #\u017a
    "Ż": "Z", #\u017b
    "ż": "z", #\u017c
    "Ž": "Z", #\u017d
    "ž": "z", #\u017e
    "ſ": "S", #\u017f
}

with open("unicode_dict.json", "w") as j:
    json.dump(unicode_dict, j, ensure_ascii=False, indent=2)
