from sqlalchemy import create_engine
from doe_data.settings_bd import Settings
import certifi

settings = Settings()

def get_engine():
    # Configure SSL context
    connect_args = {
        'sslmode': 'disable',
    }
    
    return create_engine(
        settings.DATABASE_URL,
        connect_args=connect_args
    )