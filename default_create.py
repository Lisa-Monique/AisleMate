from app import db, models

items = models.Item.query.all()
u = models.User.query.get(1)
l = models.List.query.filter_by(author=u)
i = models.Item.query.all()
for item in i:
        item.owner = l
db.session.commit()
