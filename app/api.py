# class DbConnection():
# 	def __init__(self):
# 		self.connection = psycopg2.connect(os.environ["PG_CONN_STRING"])
# 		self.cursor = connection.cursor()

# 	def conn():
#     return self.connection

#   def cur():
#     return self.cursor


def create_listings_table(connection, cursor):
  cursor.execute("CREATE TABLE Listings ( \
  id UUID NOT NULL DEFAULT gen_random_uuid(), \
  community STRING NOT NULL, \
  roomtype STRING NOT NULL, \
  gender STRING NOT NULL, \
  unit INT NOT NULL, \
  leasetype STRING NOT NULL, \
  startdate STRING NOT NULL, \
  enddate STRING NOT NULL, \
  price INT NOT NULL, \
  description STRING NULL \
  )")
  connection.commit()


def create_accounts_table(connection, cursor):
  cursor.execute("CREATE TABLE Accounts ( \
  id UUID NOT NULL DEFAULT gen_random_uuid(), \
  username STRING NOT NULL, \
  password STRING NOT NULL, \
  name STRING NOT NULL, \
  email STRING NOT NULL, \
  phone STRING NOT NULL, \
  )")
  connection.commit()


def drop_listings_table(connection, cursor):
  cursor.execute("DROP TABLE Listings")
  connection.commit()


def drop_accounts_table(connection, cursor):
  cursor.execute("DROP TABLE Accounts")
  connection.commit()


def insert_listing(connection, cursor, community, roomtype, gender, unit, leasetype, startdate, enddate, price, description=None):
  cursor.execute(
    "INSERT INTO Listings (community, roomtype, gender, unit, leasetype, startdate, enddate, price, description) VALUES \
      (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (community, roomtype, gender, unit, leasetype, startdate, enddate, price, description)
  )
  connection.commit()


def delete_rows(connection, cursor, id):
    cursor.execute("DELETE FROM Listings WHERE id = {}".format(id))
    connection.commit()


def get_all_listings(connection, cursor):
  cursor.execute("SELECT * from Listings")
  result = cursor.fetchall() 
  connection.commit()
  return result


def get_community_listings(connection, cursor, community):
  cursor.execute("SELECT * from Listings WHERE community = %s", (community,))
  result = cursor.fetchall() 
  connection.commit()
  return result