#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__='Miner'

import db
db.create_engine(user='root', password='2014', database='test', host='127.0.0.1', port=3306)
print db.select('select * from user')
n = db.update('delete from user where id=4')
print db.select('select * from user')
n = db.update('insert into user(id, name) values(?, ?)', 4, 'Jack')
print db.select('select * from user')