import pymysql as mysql
import json
import datetime
import re
import sys
import time
import os

conn = mysql.connect(host='localhost',
                     port=3306,
                     username="root",
                     pwd=os.environ.get('MYSQL_PWD'))
cur = conn.cursor()
