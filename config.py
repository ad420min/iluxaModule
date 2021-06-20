import psycopg2, telebot

b = telebot.TeleBot("", parse_mode="HTML")

hostname = 'localhost'
name = 'server'
user = 'postgres'
dbpass = 'armageddon'

db = psycopg2.connect(dbname=name, user=user, password=dbpass, host=hostname)
#sql = db.cursor()

