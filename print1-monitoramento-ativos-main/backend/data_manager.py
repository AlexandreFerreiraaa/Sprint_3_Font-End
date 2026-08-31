import json
import os

DATA_FILE = "data/equipamentos.json"

def init_db():
    # Cria a pasta se não existir
    if not os.path.exists("data"):
        os.makedirs("data")
        
    # Se o arquivo não existe ou está com 0 bytes (vazio)
    if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f) # Grava uma lista JSON vazia válida

def get_equipamentos():
    init_db()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Se por algum motivo o arquivo estiver criado mas corrompido/vazio, 
        # ele ignora o erro e retorna a lista vazia para o app não quebrar.
        return []

def add_equipamento(tag, modelo, fabricante, potencia, tensao):
    equipamentos = get_equipamentos()
    novo_eq = {
        "TAG": tag,
        "Modelo": modelo,
        "Fabricante": fabricante,
        "Potência (W)": potencia,
        "Tensão (V)": tensao
    }
    equipamentos.append(novo_eq)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(equipamentos, f, indent=4)
    return True