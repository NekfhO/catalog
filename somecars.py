from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import CarBrand, Base, BrandItem, User

engine = create_engine('sqlite:///carbrand2.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Osama Alhumaid", email="nekfh7@outlook.sa",
             picture='https://i.imgur.com/gpVzWWZ.png')
session.add(User1)
session.commit()

# Toyota

carBrandToyota = CarBrand(user_id=1, name="Toyota")

session.add(carBrandToyota)
session.commit()

brandItemToyota = BrandItem(
                    user_id=1, name="Camry", description="best in class",
                    price="$35k", category="Modren", carbrand=carBrandToyota)

session.add(brandItemToyota)
session.commit()

# Nissan

carBrandNissan = CarBrand(user_id=1, name="Nissan")

session.add(carBrandNissan)
session.commit()

brandItemNissan = BrandItem(
                    user_id=1, name="Patrol", description="Best SUV for money",
                    price="$40k", category="Modren", carbrand=carBrandNissan)

session.add(brandItemNissan)
session.commit()


# Honda

carBrandHonda = CarBrand(user_id=1, name="Honda")

session.add(carBrandHonda)
session.commit()

brandItemHonda = BrandItem(
        user_id=1, name="Accord",
        description="if you can't afford camry", price="$30k",
        category="Modren", carbrand=carBrandHonda)

session.add(brandItemHonda)
session.commit()


print "added the list!"
