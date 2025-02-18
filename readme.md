# PLY Lexer and Parser

## 📌 Project Overview
This project is an implementation of a **lexical and syntax analyzer** using **Python Lex-Yacc (PLY)**. It provides the functionality to parse and analyze a custom programming language by breaking it down into tokens and checking its grammatical structure.

## 🚀 Getting Started

### 📋 Prerequisites
Ensure you have the following dependencies installed before running the project:

- Python 3.x
- PLY (Python Lex-Yacc)

Install PLY using:
```sh
pip install ply
```

### 🔧 Installation
Clone the repository:
```sh
git clone https://github.com/your_username/PLY-Lexer-and-Parser.git
cd PLY-Lexer-and-Parser
```

## 🏗 Project Structure
```
PLY-Lexer-and-Parser/
│── main.py              # Main entry point
│── lexico.py            # Lexical analyzer using PLY
│── sintactico.py        # Syntax analyzer using PLY
│── funciones_semantico.py # Semantic verification functions
│── codigo_intermedio.py # Intermediate code generation
│── excepciones.py       # Custom exceptions handling
│── test_files/          # Test cases for different language features
│    ├── test_caracter.txt
│    ├── test_codigo_intermedio.txt
│    ├── test_function.txt
│    ├── test_function_sin_tipo.txt
│    ├── test_function_tipo_diferente.txt
│    ├── test_function_vacia.txt
│    ├── test_general.txt
│    ├── test_if.txt
│    ├── test_if_no_boolean.txt
│    ├── test_if_sin_condiciones.txt
│    ├── test_if_sin_contenido.txt
│    ├── test_let.txt
│── parser.out           # PLY-generated parser table
│── parsetab.py          # PLY-generated parse table
│── __pycache__/         # Python bytecode cache
│── PL_P3_Fernández_Mokov_memoria.pdf # Documentation of the project
```

## 🎯 Usage

### Running the Lexer
To run the **lexical analyzer**, use:
```sh
python main.py <input_file> -lex
```

### Running the Parser
To run the **syntax analyzer**, use:
```sh
python main.py <input_file> -par
```

## ✅ Testing
Several test cases are provided in the `test_files/` directory, covering various features of the language such as:
- Character parsing
- Code structure validation
- Function definition and types
- Conditional statements handling

## 🛠 Built With
- [Python 3](https://www.python.org/)
- [PLY (Python Lex-Yacc)](https://www.dabeaz.com/ply/)

## 🤝 Contributing
If you wish to contribute, feel free to fork the repository, make improvements, and submit a pull request.

---
