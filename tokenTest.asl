// Shah, Shubham B.
// sbs8554
// 2018-10-03
// --- Token test
// Just to make sure that all categories of tokens
// are scanned correctly.

// Some illegal characters.
?
  %
    $

// Tokens where the value field actually means something.
identifier        // ID
  12345           // INTEGER
    12.34e+4      // REAL
      "a string"  // STRING

// The predefined identifiers.  These are just identifiers
// as far as the tokenizer is concerned.  The semantic
// analysis step assigns their meaning.
 boolean          // ID, 'boolean'
   false          // ID, 'false'
     integer      // ID, 'integer'
       nil        // ID, 'nil'
         real     // ID, 'real'
           true   // ID, 'true'
         void     // ID, 'void'

// Reserved words.
and               // AND
  by              // BY
    const         // CONST
      div         // DIV
        do        // DO
          elif    // ELIF
        else      // ELSE
      exit        // EXIT
    extends       // EXTENDS
  fi              // FI
for               // FOR
  func            // FUNC
    if            // IF
      loop        // LOOP
        mod       // MOD
          next    // NEXT
        not       // NOT
      of          // OF
    or            // OR
  read            // READ
record            // RECORD
  return          // RETURN
    then          // THEN
      to          // TO
        var       // VAR
          while   // WHILE
        write     // WRITE

// Operators and delimiters.
=                 // ASSIGN
  @               // AT
    :             // COLON
      ,           // COMMA
        /         // DIVIDE
          ==      // EQ
        >=        // GE
      >           // GT
    {             // LBRACE
  [               // LBRACKET
<=                // LE
  (               // LPAREN
    <             // LT
      -           // MINUS
        *         // MULTIPLY
          <>      // NE
        .         // PERIOD
      +           // PLUS
    ->            // PTR
  }               // RBRACE
]                 // RBRACKET
  )               // RPAREN
    ;             // SEMICOLON
