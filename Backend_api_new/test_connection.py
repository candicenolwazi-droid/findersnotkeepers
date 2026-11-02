from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://db_user:CHANGE_ME@localhost/findernotkeepers_test")
conn = engine.connect()
print("✅ Connected to PostgreSQL!")
conn.close()



#MYSQL
# from sqlalchemy import create_engine, text  # <-- import text

# DB_URI = "mysql+pymysql://db_user:CHANGE_ME@localhost/findernotkeepers_test"
# engine = create_engine(DB_URI)

# try:
#     with engine.connect() as conn:
#         result = conn.execute(text("SELECT DATABASE();"))  # <-- wrap SQL in text()
#         db_name = result.fetchone()[0]
#         print(f"Connected successfully to database: {db_name}")
# except Exception as e:
#     print("Connection failed!")
#     print(e)
