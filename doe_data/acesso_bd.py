from sqlalchemy import create_engine, text
from doe_data.settings_bd import Settings
import os

settings = Settings()

DATABASE_URL = (
    f"postgresql://{settings.USER_DB}:{settings.PASSWORD_DB}"
    f"@{settings.HOST}:{settings.PORT}/{settings.DATABASE}"
)

def get_engine():
    return create_engine (DATABASE_URL)

## TESTE CONEXÃO AO DB
# try:
#     with engine.connect() as connection:
#         result = connection.execute(text("SELECT 1"))
#         print("✅ Conexão bem-sucedida! Resultado:", result.scalar())
# except Exception as e:
#     print("❌ Erro ao conectar ao banco de dados:")
#     print(e)