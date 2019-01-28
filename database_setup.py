from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,backref
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class CarBrand(Base):
    __tablename__ = 'car_brand'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User,backref=backref("CarBrand", cascade="all,delete"))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class BrandItem(Base):
    __tablename__ = 'brand_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    category = Column(String(250))
    carbrand_id = Column(Integer, ForeignKey('car_brand.id'))
    carbrand = relationship(CarBrand,backref=backref("BrandItem", cascade="all,delete"))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User,backref=backref("BrandItem", cascade="all,delete"))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'category': self.category,
        }


engine = create_engine('sqlite:///carbrand2.db')


Base.metadata.create_all(engine)
