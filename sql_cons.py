# F_Name STRING ,
# Age_Id STRING,
# Phone_Num INTEGER,
# Lang_Level STRING,
# Lang STRING,
import sqlite3
conn = sqlite3.connect('table_0f_tables.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Users(
TG_ID INTEGER ,
F_Name STRING ,
Age_Id STRING,
Phone_Num INTEGER,
Lang_Level STRING,
Lang INTEGER ,
Stage INTEGER

)
''')
first_insert = '''
INSERT INTO Users VALUES ('{}',' ',' ',' ',' ',' ','{}')
'''
get_id = '''
SELECT TG_ID 
FROM Users
Where TG_ID = '{}'
'''
upd_name = '''
UPDATE Users 
SET F_Name = '{}' 
WHERE TG_ID = '{}'
'''
select_name = '''
SELECT F_Name
From Users
WHERE TG_ID = '{}'
'''

update_phone_num = '''
UPDATE Users 
SET Phone_Num = '{}' 
WHERE TG_ID = '{}'
'''
select_num = '''
SELECT Phone_Num 
FROM Users
WHERE TG_ID = '{}'
'''
get_level = '''
UPDATE Users 
SET Lang_level = '{}' 
WHERE TG_ID = '{}'
'''
select_level = '''
SELECT Lang_level
FROM Users
WHERE TG_ID = '{}'
'''
select_age = '''
SELECT Age_Id
FROM Users
WHERE TG_ID = '{}'
'''
get_ageid = '''
UPDATE Users 
SET Age_Id = '{}' 
WHERE TG_ID = '{}'
'''
lang = '''
UPDATE Users
SET lang = '{}'
WHERE TG_ID = '{}'

'''
lang_select = '''
SELECT Lang
FROM Users
WHERE TG_ID = '{}'
'''

stagee = '''
UPDATE Users
SET Stage = '{}'
WHERE TG_ID = '{}'
'''
stage = '''
SELECT Stage
FROM Users
WHERE TG_ID = '{}'
'''
conn.commit()