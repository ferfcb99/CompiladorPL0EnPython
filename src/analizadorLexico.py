from ast import For
import ply.lex as lex
import re 
import codecs
import os
import sys

reservadas = ['BEGIN', 'END',' IF', 'THEN', 'DO', 'CALL', 'CONST','VAR', 'PROCEDURE', 'OUT', 'IN', 'ELSE'];
# public
# int
# final
# static 

tokens = reservadas + ['ID', 'NUMBER', 'PLUS', 'MINUS','TIMES','DIVIDE','ODD', 'ASSIGN', 'NE', 'LT', 'LTE', 'GT', 'GTE', 'LPARENT', 'RPARENT', 'COMMA', 'SEMMICOLOM', 'DOT', 'UPDATE'];

t_ignore = r'\t '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='


        
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
        
    return t

def t_COMMENT(t):
    r'\#.*'
    pass;


def t_newline(t):
    r'\n+';
    t.lexer.lineno ==  t.lexer.lineno + len(t.value);
    
        
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value);
    return t;

def t_error(t):
    print("Caracter ilegal dentro del lenguaje '%s'" % t.value[0])
    t.lexer.skip(1)

def buscaFichero(directorio):
    ficheros= []
    numArchivo = ''
    respuesta = False
    count = -1
    # guardar los archivos
    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    # contar archivos
    for file in files:
        print(str(count) + ". " + file)
        count = count + 1

    while respuesta == False:
        numArchivo = raw_input("Numero de test: ")
        for file in files: 
            if file == files[int(numArchivo)-1]
            return True
            break
        
    print("Elegiste {}".format(files[int(numArchivo)]))
    
    return files[int(numArchivo)- 1]
    
directorio = '../test/'
archivo = buscaFichero(directorio)