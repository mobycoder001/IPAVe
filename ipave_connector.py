#!/usr/bin/env python3

'''query the database'''

import psycopg2

conn = psycopg2.connect('ipave.db')

c = conn.cursor()
c.execute('SELECT * FROM ipave')
print c.fetchall()
conn.close()