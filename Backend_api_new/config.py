#FOr my SQL
# # password = "CHANGE_ME"
# # encoded_password = quote_plus(password)
# myUsername="db_user"
# password="CHANGE_ME"
# dbhost="localhost"
# dbname="findernotkeepers_test"
# SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{myUsername}:{password}@{dbhost}/{dbname}"
# SQLALCHEMY_TRACK_MODIFICATIONS=False

#For pgAdmin
myUsername = "db_user"
password = "CHANGE_ME"
dbhost = "localhost"
dbname = "findernotkeepers_test"

SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{myUsername}:{password}@{dbhost}/{dbname}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
