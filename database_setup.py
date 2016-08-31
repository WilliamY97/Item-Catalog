from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Catalog(Base):
    __tablename__ = 'catalog'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return catalog data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'owner': self.user.name
        }


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    catalog_id = Column(Integer, ForeignKey('catalog.id'))
    catalog = relationship(Catalog)

    @property
    def serialize(self):
        """Return list of categories for a given catalog in easily
        serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'parent_catalog': self.catalog.name
        }


class RecordTemplate(Base):
    __tablename__ = 'record_template'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    template_fields = relationship("FieldTemplate",
                                   back_populates="record_template")


class FieldTemplate(Base):
    __tablename__ = 'field_template'

    id = Column(Integer, primary_key=True)
    label = Column(String(250), nullable=False)
    kind = Column(Enum('short_text',
                       'long_text',
                       'drop_down',
                       'check_box',
                       'radio'), nullable=False)
    order = Column(Integer, nullable=False)
    record_template_id = Column(Integer, ForeignKey('record_template.id'))
    record_template = relationship("RecordTemplate",
                                   back_populates='template_fields')


class Option(Base):
    __tablename__ = 'option'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    field_template_id = Column(Integer, ForeignKey('field_template.id'))
    field_template = relationship(FieldTemplate)


class Record(Base):
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    record_template_id = Column(Integer, ForeignKey('record_template.id'))
    category_id = Column(Integer, ForeignKey('category.id'))
    record_template = relationship(RecordTemplate)
    category = relationship(Category)

    @property
    def serialize(self):
        """Return list of records for a given categories in easily
        serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'parent_category': self.category.name,
            'parent_catalog': self.category.catalog.name
        }


class Field(Base):
    __tablename__ = 'field'

    id = Column(Integer, primary_key=True)
    value = Column(String(500), nullable=False)
    record_id = Column(Integer, ForeignKey('record.id'))
    field_template_id = Column(Integer, ForeignKey('field_template.id'))
    record = relationship(Record)
    field_template = relationship(FieldTemplate)

    @property
    def serialize(self):
        """Return record data in easily serializeable format"""
        return {
            'id': self.id,
            'field_label': self.field_template.label,
            'field_value': self.value,
            'parent_record': self.record.name,
            'parent_category': self.record.category.name,
            'parent_catalog': self.record.category.catalog.name
        }


engine = create_engine('sqlite:///catalogizer.db')

Base.metadata.create_all(engine)
