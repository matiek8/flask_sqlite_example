from . import db


tag_identifier = db.Table('tag_identifier',
    db.Column('file_id', db.Integer, db.ForeignKey('files.file_id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.tag_id'))
)


class Tag(db.Model):
    __tablename__ = 'tags'
    tag_id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(64))


class File(db.Model):
    __tablename__ = 'files'
    file_id = db.Column(db.Integer, primary_key=True)
    file_content = db.Column(db.String(128))
    tags = db.relationship("Tag", secondary=tag_identifier)

