from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from vviewer.orm import session, Base
# from vviewer.models.sources import Sources


class BamFiles(Base):
    __tablename__ = 'bam_files'
    id = Column(Integer, primary_key=True)
    original_filename = Column(String(255))
    file_path = Column(String(255))
    date_sequenced = Column(DateTime)
    sequencer = Column(String(255))
    sample_id = Column(Integer, ForeignKey("samples.id"))
    sequence_integer_id = Column(Integer, ForeignKey("sequence_centers.id"))
    read_group = Column(String(255))
    permissions = Column(JSONB)
    created_by = Column(String(255))
    created_on = Column(DateTime(timezone=True))

    def __str__(self):
        return f'BamFiles(id={self.id}, original_filename={self.original_filename}, file_path={self.file_path})'

    @classmethod
    def find_bamFiles(cls):
        bamFiles = session.query(cls).all()
        if bamFiles:
            bamFilesList = [u.__dict__ for u in bamFiles]
            print("bamFilesList", bamFilesList)
        return "Got bamFiles"

    @classmethod
    def find_by_bamFile_id(cls, _id):
        result = session.query(cls).filter(cls.id == _id).first()
        return repr(result)

    @classmethod
    def create_bamFile(cls, bamFile):
        session.add(bamFile)
        session.commit()
        return "BamFile added"

    @classmethod
    def delete_bamFile(cls, _id):
        session.query(cls).filter(cls.id == _id).delete()
        session.commit()
        return "BamFile deleted"
