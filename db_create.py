from app.models import Tag, File, tag_identifier
from app import db

db.create_all()
file_1 = File(file_content="bla")
file_2 = File(file_content="test")
file_3 = File(file_content="bla test")

tag_1 = Tag(tag_name='news')
tag_2 = Tag(tag_name='politics')
tag_3 = Tag(tag_name='art')

db.session.add_all([file_1, file_2, file_3, tag_1, tag_2, tag_3])
db.session.commit()

file_1.tags.append(tag_1)
file_1.tags.append(tag_2)
file_2.tags.append(tag_3)
file_3.tags.append(tag_1)
file_3.tags.append(tag_2)
file_3.tags.append(tag_3)

# statement = tag_identifier.insert().values(file_id=1, tag_id=1)
# statement1 = tag_identifier.insert().values(file_id=1, tag_id=2)
# statement2 = tag_identifier.insert().values(file_id=1, tag_id=3)
# statement3 = tag_identifier.insert().values(file_id=2, tag_id=1)
# statement4 = tag_identifier.insert().values(file_id=3, tag_id=2)
# statement5 = tag_identifier.insert().values(file_id=3, tag_id=3)
# db.session.execute(statement)
# db.session.execute(statement1)
# db.session.execute(statement2)
# db.session.execute(statement3)
# db.session.execute(statement4)
# db.session.execute(statement5)

db.session.commit()
