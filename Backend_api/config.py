#FOr my SQL
myUsername="db_user"
password="CHANGE_ME"
dbhost="localhost"
dbname="findernotkeepers"
SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{myUsername}:{password}@{dbhost}/{dbname}"
SQLALCHEMY_TRACK_MODIFICATIONS=False