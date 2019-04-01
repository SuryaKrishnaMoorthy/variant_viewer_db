from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from vviewer.orm import session, Base
from vviewer.models.sources import Sources


class Studies(Base):
    __tablename__ = 'studies'
    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, ForeignKey(Sources.id))
    permissions = Column(JSONB)

    def __str__(self):
        return f'Studies(id={self.id}, permissions={self.permissions}'

    @classmethod
    def find_studies(cls):
        studies = session.query(cls).all()
        # studiesList = [u.__dict__ for u in studies]
        return str(studies)

    @classmethod
    def find_by_study_id(cls, _id):
        result = session.query(cls).filter(cls.id == _id).first()
        return repr(result)

    @classmethod
    def create_study(cls, study):
        session.add(study)
        session.commit()
        return "Added study"
