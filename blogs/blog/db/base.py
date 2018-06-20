from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

eng = create_engine('postgresql://first:0329@localhost/blogs')
Base = declarative_base()
Base.metadata.bind = eng