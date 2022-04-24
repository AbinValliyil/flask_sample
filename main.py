from flask import  Flask,request, jsonify
from itsdangerous import Serializer
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String,Boolean,Integer,Column,DateTime,ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import  relationship



app = Flask('__name__')

engine=create_engine('postgresql://postgres:123@localhost/Arclif',echo=True) 



print("Database ****** connected")

Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionLocal=sessionmaker(bind = engine)


class flask(Base):
    __tablename__ ='flask_samole'
    id            = Column(Integer,primary_key=True,autoincrement=True)
    silver        = Column(Integer,nullable=False)
    golden        = Column(Integer,nullable=False)


Base.metadata.create_all(bind=engine)             
db = SessionLocal()




# Api 

@app.route('/')
def im():
    return {'message':'server connect successs'}

 


@app.route('/p', methods=['POST'])
def h():
    new_client = flask(silver =0,golden =5)
    db.add(new_client)
    db.commit() 
    return 'ok'




@app.route('/r', methods=['GET'])
def r():
    id = request.args.get('id')
    d=db.query(flask).filter(flask.id==id).first()
    return 	jsonify({'golden':d.golden,'silver':d.silver})
if __name__ == "__main__":
    app.run(debug=True)


