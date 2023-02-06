# class DbConnection():
# 	def __init__(self):
# 		self.connection = psycopg2.connect(os.environ["PG_CONN_STRING"])
# 		self.cursor = connection.cursor()

# 	def conn():
#     return self.connection

#   def cur():
#     return self.cursor


def create_table(connection, cursor):
  cursor.execute("CREATE TABLE Listings ( \
  id UUID NOT NULL DEFAULT gen_random_uuid(), \
  community STRING NOT NULL, \
  unit INT NOT NULL, \
  leasetype STRING NOT NULL, \
  roomtype STRING NOT NULL, \
  startdate STRING NOT NULL, \
  enddate STRING NOT NULL, \
  gender STRING NOT NULL, \
  price INT NOT NULL, \
  description STRING NULL \
  )")
  connection.commit()


def drop_table(connection, cursor):
  cursor.execute("DROP TABLE Listings")
  connection.commit()


def insert_data(connection, cursor, community, unit, leasetype, roomtype, startdate, enddate, gender, price, description=None):
  cursor.execute(
    "INSERT INTO Listings (community, unit, leasetype, roomtype, startdate, enddate, gender, price, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (community, unit, leasetype, roomtype, startdate, enddate, gender, price, description)
  )
  connection.commit()


def delete_rows(connection, cursor, id):
    cursor.execute("DELETE FROM Listings WHERE id = {}".format(id))
    connection.commit()


def get_data(connection, cursor):
  cursor.execute('''SELECT * from Listings''')
  result = cursor.fetchall()
  connection.commit()
  return result

# insert_data('VDC', 62714, 'Sublet', 'Quad', 'February', 'June', 'Male', 1004, 'hi')
# delete_rows(0x85e0a2aa165b4893a411a9339fc17df7)
#get_data()