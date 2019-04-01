from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from vviewer.orm import session, Base
from vviewer.models.samples import Samples
import json


class Sources(Base):
    __tablename__ = 'sources'
    id = Column(Integer, primary_key=True)
    mrn = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    gender = Column(String(6))
    dob = Column(DateTime)
    disease_state = Column(JSONB)
    maternal_id = Column(Integer)
    paternal_id = Column(Integer)
    family_id = Column(Integer)
    permissions = Column(JSONB)
    child = relationship(Samples, backref="sources", passive_deletes=True)
    created_by = Column(String(255))
    created_on = Column(DateTime(timezone=True))

    def __str__(self):
        return f'Sources=(id={self.id}, first_name={self.first_name}, last_name={self.last_name})'

    def __repr__(self):
        return self.__str__()

    @classmethod
    def find_sources(cls):
        sources = session.query(cls).all()
        sourcesList = [u.__dict__ for u in sources]
        print(sources, sourcesList)
        return repr(sources)

    @classmethod
    def find_by_source_id(cls, _id):
        result = session.query(cls).filter(cls.id == _id).first()
        return repr(result)

    @classmethod
    def create_source(cls, source):
        session.add(source)
        session.commit()
        return "Added Source"

    @classmethod
    def delete_source(cls, _id):
        session.query(cls).filter(cls.id == _id).delete()
        session.commit()
        return "Source deleted"
