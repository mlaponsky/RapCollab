import pymysql as mysql
import json
import datetime
import re
import sys
import time
import os

from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


conn = mysql.connect(host='localhost',
                     port=3306,
                     username="root",
                     pwd=os.environ.get('MYSQL_PWD'))
cur = conn.cursor()

BASE_URL = "http://www.ohhla.com/all.html"
SECTION_LINKS = ['xx', 'a', 'b', 'c', 'd', 'e',
                 'all_two', 'all_three', 'all_four', 'all_five']
BASE_DIV = "leftmain"
