from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from vviewer.orm import session, Base
# from vviewer.models.sources import Sources


class Samples(Base):
    __tablename__ = 'samples'
    id = Column(Integer, primary_key=True)
    tissue_type = Column(String(255))
    tumor_sample = Column(Boolean)
    date_collected = Column(DateTime)
    date_used = Column(DateTime)
    phenotype = Column(JSONB)
    source_id = Column(Integer, ForeignKey("sources.id", ondelete='CASCADE'))
    permissions = Column(JSONB)
    created_by = Column(String(255))
    created_on = Column(DateTime(timezone=True))

    def __str__(self):
        return f'Samples(id={self.id}, tissue_type={self.tissue_type}, tumor_sample={self.tumor_sample})'

    def __repr__(self):
        return self.__str__()

    def __matmul__(self, other):
        # compare tissue samples for quality metrics , lookuo patient the sample belongs to and do population stratification across childrens dataset
        return f'{self.tissue_type} and {other.tissue_type}'

    @classmethod
    def find_samples(cls):
        samples = session.query(cls).all()
        if samples:
            samplesList = [u.__dict__ for u in samples]
            print("samplesList", samplesList)
        return "Got Samples"

    @classmethod
    def find_by_sample_id(cls, _id):
        result = session.query(cls).filter(cls.id == _id).first()
        return repr(result)

    @classmethod
    def create_sample(cls, sample):
        session.add(sample)
        session.commit()
        return "Sample added"

    @classmethod
    def delete_sample(cls, _id):
        session.query(cls).filter(cls.id == _id).delete()
        session.commit()
        return "Sample deleted"
