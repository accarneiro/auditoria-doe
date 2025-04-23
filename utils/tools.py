import re

def normalize_text(text):
    text = re.sub(r"\s+", " ", text) # converte tudo que for espaço, tab, quebra de linha etc
    text = text.replace("\u00a0", " ") # NBSP (non-breaking space)
    return text.strip()

def highlight_text(texto_base, termo):
    if not termo or not isinstance(termo, str):
        return texto_base
    texto_base_norm = normalize_text(texto_base)
    termo_norm = normalize_text(termo)
    escaped = re.escape(termo_norm)

    try:
        match = re.search(escaped, texto_base_norm, flags=re.IGNORECASE)
        if not match:
            return texto_base #nada encontrado
        
        # Recupera o trecho original (exato como aparece no texto_base)
        start, end = match.span()
        trecho_original = texto_base_norm[start:end]

        #Agora insere o <mark> no texto_base (bruto), usando o trecho original
        return texto_base.replace(trecho_original, f"<mark>{trecho_original}</mark>", 1)
    except Exception as e:
        return texto_base




