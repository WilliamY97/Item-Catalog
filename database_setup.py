"""Configuration"""

"""
Beginning of File:
Imports all modules needed & creates instance of declarative base
"""

import sys

from sqlalchemy import
Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import
declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

"""
End of File:
Creates (or connects) the database and adds tables and columns
"""

engine = create_engine(
'sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)