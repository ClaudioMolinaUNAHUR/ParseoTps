import os
import sys
import json
from scanner.scanner import lexer

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

def like_json(data):
    return json.dumps(data, indent=2, ensure_ascii=False)

def main():
    data = """
    #start
    num x: 10
    //comentario
    if(x > 5) {
        console("ok")
    } else {
        console("no")
    }
    #end
    """

    lexer.input(data)

    print("Tokens encontrados:")
    for tok in lexer:
        print(tok)
        
if __name__ == "__main__":
    main()
