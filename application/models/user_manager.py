from application import app
import battleship_db

def is_email_duplicated(email) :
    query = "SELECT ID FROM user WHERE email = '%s'" % email
    return [True, False][battleship_db.count(query) == 0]

def add_user(email, password, school_id, members) :
    salt = app.config['SALT']
    query = "INSERT INTO user (email, password, school_id) VALUES " + "('%s', password('%s'), '%s')" % (email, password + salt, school_id)
    res = battleship_db.insert(query)
    user_id = res.connection.insert_id()
    query = "INSERT INTO team_member (user_id, member_name) VALUES " + ",".join(["('%d', '%s')" % (user_id, member) for member in members])
    return battleship_db.insert(query)

def get_users(where) :
    query = "SELECT * FROM user usr LEFT JOIN (SELECT user_id, GROUP_CONCAT(member_name) members FROM team_member GROUP BY user_id) team ON usr.ID = team.user_id " + where
    return battleship_db.select(query)