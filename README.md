# Crudfcts
make a git clone to the project https://github.com/FatmaElk/Crudfcts.git

Open visual studio and import the project

=> Install pyenv:
curl https://pyenv.run | bash
rm -rf /home/test/.pyenv
curl https://pyenv.run | bash
pyenv install 3.7.4
pyenv shell 3.7.4
pyenv which python
=================
=> Install dependencies:
pip install -r requirements.txt
pip list
================
=> Run project and check if localhost:5000 is working fine
python3 api.py
=================
=> Create db and check table:
python
from api import db
db.create_all()
exit()
sqlite3 base.db
.tables
.exit
================
=> To test with postman tool:
GET*http://localhost:5000/users => get all users
GET*http://localhost:5000/user/2 => get user with id 2
POST*http://localhost:5000/user/1 => insert first user id 1
{"id": 1, "firstname" : "Charelotte", "lastname" : "Linlin" , "age" : 75 }
PUT* http://localhost:5000/user/1 => update age it's static in the code :p "user.age = 100" not enough time to check that
DELETE* http://localhost:5000/user/1 => delete user with id 1
