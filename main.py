from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"

    user1 = User()
    user1.surname = "Elton"
    user1.name = "Jhon"
    user1.age = 73
    user1.position = "passenger"
    user1.speciality = "singer"
    user1.address = "module_4A"
    user1.email = "Elton_GOAT@mars.org"

    user2 = User()
    user2.surname = "Uzumaki"
    user2.name = "Naruto"
    user2.age = 33
    user2.position = "VIP-guest"
    user2.speciality = "hokage"
    user2.address = "module_2"
    user2.email = "you_are_my_friend@mars.org"

    user3 = User()
    user3.surname = "Drawde"
    user3.name = "Nedwons"
    user3.age = 37
    user3.position = "passenger"
    user3.speciality = "refugee"
    user3.address = "module_4B"
    user3.email = "NOT_EDWARD_SNOWDEN@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.add(user2)
    db_sess.add(user1)
    db_sess.add(user3)
    db_sess.commit()

    # app.run()


if __name__ == '__main__':
    main()