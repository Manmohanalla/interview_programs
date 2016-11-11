import pymysql.cursors
import logging
from datetime import date
import os

# create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

#using date module to create filename
date = date.today()
date=str(date)
logfile=date+'.dat'

#look for file and create if not available
if not os.path.exists("logfile"):
	file(logfile, "wb+")

logging.basicConfig(filename=logfile, level=logging.INFO)

# create log handler and set level to debug
lh = logging.StreamHandler()
lh = logging.FileHandler("deviceGet.log")
lh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# add formatter to lh
lh.setFormatter(formatter)

# add lh to logger
logger.addHandler(lh)

# create console handler and set level to debug
consoleHandler = logging.StreamHandler()

# add formatter to consolehandler
consoleHandler.setFormatter(formatter)

# add console to logger
logger.addHandler(consoleHandler)

class Mysql(object):

	def connection(self):

		# Connect to the database
		connection = pymysql.connect()

		msg='conection established with db'
		logging.info(msg)

		return connection

	def create_table(self):
		
		# Connect to the database
		connection = self.connection()
		try:	
			with connection.cursor() as cursor:
				#Create Table
				sql = "CREATE TABLE `test` (`id` int(11) NOT NULL ,`email` varchar(255) NOT NULL,`name` varchar(255) NOT NULL)"
				cursor.execute(sql)
				#Commit the table
				connection.commit()

				msg='table created'
				logging.info(msg)
		finally:
			#clossing connection
			connection.close()

			msg='connection closed'
			logging.info(msg)

	def insert_table(self,id,email,name):

		# Connect to the database
		connection = self.connection()
		try:
			with connection.cursor() as cursor:
				# Create a new record
				sql = "INSERT INTO `test` (`id`,`email`, `name`) VALUES (%s,%s, %s)"
				cursor.execute(sql, (id,email,name))

				msg= 'values insterted into tabe'
				logging.info(msg)
			# connection is not autocommit by default. So you must commit to save
			# your changes.
			connection.commit()

		finally:
			connection.close()

			msg='connection closed'
			logging.info(msg)

	def select_table(self,id):

		# Connect to the database
		connection = self.connection()
		try:
			with connection.cursor() as cursor:
				# Read a single record
				sql = "SELECT * FROM `test` WHERE `id`=%s"
				cursor.execute(sql, (id,))
				result = cursor.fetchone()

				msg='select query performed'
				logging.info(msg)
		
		finally:
			connection.close()

			msg='connection closed'
			logging.info(msg)
		return result
		
sql = Mysql()
sql.select_table(1)
