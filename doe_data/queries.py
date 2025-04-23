from sqlalchemy import text
from doe_data.acesso_bd import get_engine

def get_publicacoes():
    query = text("SELECT link, id, conteudo_link FROM vw_publicacao")
    with get_engine().connect() as conn:
        result = conn.execute(query)
        return result.fetchall()

def get_atos(publicacao_id):
    query = text ("""
                    SELECT conteudo_ato
                    FROM processing.ato
                    WHERE publicacao_id = :id
                    """)
    with get_engine().connect() as conn:
        result = conn.execute(query, {"id": publicacao_id})
        return result.fetchall()