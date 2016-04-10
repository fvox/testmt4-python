#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import ConfigParser
import MySQLdb

cfg = ConfigParser.ConfigParser()
cfg.read('database.ini')

dbHost = cfg.get('mysql', 'host')
dbUser = cfg.get('mysql', 'username')
dbPasswd = cfg.get('mysql', 'password')
dbSchema = cfg.get('mysql', 'database')

db = MySQLdb.connect(dbHost, dbUser, dbPasswd, dbSchema)
cursor = db.cursor()

print 'Por qual tipo você deseja pesquisar?'
print '1) Produtoras'
print '2) Genero'
print '3) Nome do filme'
opc = raw_input('')
opc = int(opc)

print 'Por qual termo você desejar pesquisar?'
term = raw_input('')

def searchByProdutora(term):
    sqlQuery = '''
SELECT f.nome, f.ano, f.sinopse
FROM filme f
JOIN produtora p
  ON f.produtora_id = p.id
WHERE p.nome LIKE %s
'''
    try:
        cursor.execute(sqlQuery, ('%' + term + '%'));
    except:
        print(cursor._last_executed)
        raise

    for filme in cursor.fetchall():
        print "Nome: %s" % filme[0]
        print "Ano de lançamento: %s" % filme[1]
        print "Sinopse: %s " % filme[2]
        print
    return

def searchByGenero(term):
    sqlQuery = '''
SELECT f.nome, f.ano, f.sinopse
FROM filme f
JOIN genero g
  ON f.genero_id = g.id
WHERE g.name LIKE ?
'''

    try:
        cursor.execute(sqlQuery, ('%' + term + '%'));
    except:
        print(cursor._last_executed)
        raise

    for filme in cursor.fetchall():
        print "Nome: %s" % filme[0]
        print "Ano de lançamento: %s" % filme[1]
        print "Sinopse: %s " % filme[2]
        print
    return

def searchByFilmeName(term):
    sqlQuery = '''
SELECT nome, ano, sinopse
FROM filme
WHERE nome LIKE = %s
'''
    try:
        cursor.execute(sqlQuery, ('%' + term + '%'));
    except:
        print(cursor._last_executed)
        raise

    for filme in cursor.fetchall():
        print "Nome: %s" % filme[0]
        print "Ano de lançamento: %s" % filme[1]
        print "Sinopse: %s " % filme[2]
        print
    return    

if opc == 1:
    searchByProdutora(term)
elif opc == 2:
    searchByGenero(term)
elif opc == 3:
    searchByFilmeName(term)
else:
    print 'Você digitou uma opção inválida.'

print

db.close()

