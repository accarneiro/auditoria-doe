import re


def destacar_trechos(texto, trechos_para_destacar):
    for trecho in trechos_para_destacar:
        if trecho in texto:
            texto = texto.replace(
                trecho,
                f"<span style='background-color: #FFE4C4; color: black;'>{trecho}</span> ┃",
            )
    return texto


def remover_hifen_lista(texto):
    # Remove hífen no início de linha seguido por espaço
    texto = re.sub(r"(?m)^-\s+", "", texto)
    # Substitui o caractere corrompido '' (U+F0B0) por 'º' (U+00BA)
    texto = texto.replace("", "º")
    return texto