from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import JSONB


Base = declarative_base()


class Samples(Base):
    __tablename__ = 'samples'
    id = Column(Integer, primary_key=True)
    tissue_type = Column(String(255))
    tumor_sample = Column(Boolean)
    date_collected = Column(DateTime)
    date_used = Column(DateTime)
    phenotype = Column(JSONB)
    source_id = Column(Integer)
    permissions = Column(JSONB)
    created_by = Column(String(255))
    created_on = Column(DateTime(timezone=True))


class BamFiles(Base):
    __tablename__ = 'bam_files'
    id = Column(Integer, primary_key=True)
    original_filename = Column(String(255))
    file_path = Column(String(255))
    date_sequenced = Column(DateTime)
    sequencer = Column(String(255))
    sample_id = Column(Integer)
    sequence_integer_id = Column(Integer)
    read_group = Column(String(255))
    permissions = Column(JSONB)
    created_by = Column(String(255))
    created_on = Column(DateTime(timezone=True))


class Studies(Base):
    __tablename__ = 'studies'
    id = Column(Integer, primary_key=True)
    source_id = Column(Integer)
    permissions = Column(JSONB)


class SequenceCenters(Base):
    __tablename__ = 'sequence_centers'
    id = Column(Integer, primary_key=True)
    source_id = Column(Integer)
    permissions = Column(JSONB)


def init_db(uri):
    engine = create_engine(uri, convert_unicode=True, echo=False)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session
