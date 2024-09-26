from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine=create_engine('postgresql://postgres:Vamsi%40060500@localhost/pizza-delivery',
    echo=True    
)

Base=declarative_base()

Session=sessionmaker()
