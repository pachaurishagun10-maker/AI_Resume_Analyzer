from sqlalchemy import create_engine
from sqlalchemy.orm import declerative_base, sessionmaker

DATABASE_URL = An1QsGcFtTKrIWum

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl":{
            "ssl":True
        }
    }
)