from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('peewee_shopping_list.db')

class Item(Model):
    description = CharField()

    class Meta:
        database = db

def add_items_to_db():
    global db
    items = [
        { "description": 'Corn' },
        { "description": 'Potatoes' },
        { "description": 'Plate' },
        { "description": 'Glass' },
        { "description": 'Hoodies' }
        ]
    for item in items:
        Item.create(description=item['description'])

if __name__ == "__main__":
    db.connect()
    db.create_tables([Item])
    add_items_to_db()
