# PLY Lexer and Parser

This repository contains an implementation of a lexer and parser using [PLY (Python Lex-Yacc)](https://www.dabeaz.com/ply/). The project demonstrates how to build a complete compiler front-end with lexical analysis, syntactic analysis, semantic actions, and intermediate code generation using PLY.

## Overview

The project is structured to separate the different phases of compilation:

- **Lexical Analysis:** Implemented in `lexico.py` to tokenize the input source code.
- **Syntactic Analysis:** Handled by `sintactico.py` to parse the tokens and build a parse tree.
- **Semantic Analysis & Intermediate Code Generation:** Semantic functions are defined in `funciones_semantico.py`, while intermediate code generation is performed in `codigo_intermedio.py`.
- **Error Handling:** Custom exceptions and error management are provided in `excepciones.py`.

A detailed project report/documentation is included in `PL_P3_Fernández_Mokov_memoria.pdf`.

## Features

- **Complete Lexer and Parser:** Built entirely with PLY.
- **Semantic Actions:** Integrated semantic functions during parsing.
- **Intermediate Code Generation:** Produces an intermediate representation of the source code.
- **Robust Error Handling:** Custom exception handling for both lexical and syntactic errors.
- **Testing Suite:** Includes test files in the `test_files` directory to validate compiler phases.

## Requirements

- Python 3.x
- [PLY (Python Lex-Yacc)](https://www.dabeaz.com/ply/)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/samufern/PLY-Lexer-and-Parser.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd PLY-Lexer-and-Parser
   ```
3. **(Optional) Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install PLY:**
   ```bash
   pip install ply
   ```

## Usage

Run the main driver to start the compilation process:
```bash
python main.py
```
This will execute the lexer, parser, semantic analysis, and intermediate code generation on the provided source code.

## File Structure

```
├── codigo_intermedio.py       # Intermediate code generator
├── codigo_intermedio.out      # Output from intermediate code generation
├── excepciones.py             # Custom exception handling
├── funciones_semantico.py     # Semantic analysis functions
├── lexico.py                  # Lexical analyzer using PLY
├── main.py                    # Main entry point for the compiler
├── parser.out                 # PLY parser debugging output
├── parsetab.py                # PLY parser table (generated)
├── sintactico.py              # Syntactic analyzer using PLY
├── test_files/                # Directory containing test source code files
└── PL_P3_Fernández_Mokov_memoria.pdf  # Project report/documentation
```

## Testing

To run tests on sample source files, execute:
```bash
python main.py --test
```
Test results will be generated using the files in the `test_files` directory.

## Documentation

For further details on the design and implementation, please refer to the documentation in `PL_P3_Fernández_Mokov_memoria.pdf`.

## Contributing

Contributions, suggestions, and bug reports are welcome. Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. (If a LICENSE file is provided, refer to it for details.)

## Contact

For any inquiries, please contact the repository owner.
