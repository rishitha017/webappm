import dataset

db = dataset.connect('sqlite:///shopping_list.db')

try:
    db['list'].drop()
except:
    pass

db.begin()
try:
    table = db['list']
    items = [
        { "description": 'Corn' },
        { "description": 'Potatoes' },
        { "description": 'Plate' },
        { "description": 'Glass' },
        { "description": 'Hoodies' }
        ]
    table.insert_many(items)
    db.commit()
except:
    db.rollback()
