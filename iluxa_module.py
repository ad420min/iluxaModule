import telebot.types, datetime
from config import db
from config import b as bot

sql = db.cursor()

def stages(user_id, new_stage=None):
    sql.execute(f"""CREATE TABLE IF NOT EXISTS stages(
    user_id TEXT,
    stage TEXT
    )""")
    db.commit()
    if new_stage == None:
        sql.execute(f"SELECT * FROM stages WHERE user_id = '{str(user_id)}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO stages VALUES('{str(user_id)}', 'None')")
            db.commit()
            return "None"
        else:
            st = None
            sql.execute(f"SELECT * FROM stages WHERE user_id = '{str(user_id)}'")
            for i in sql.fetchall():
                st = str(i[1])
            return st


    elif new_stage != None:
        sql.execute(f"SELECT * FROM stages WHERE user_id = '{str(user_id)}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO stages VALUES('{str(user_id)}', '{str(new_stage)}')")
            db.commit()
        else:
            sql.execute(f"UPDATE stages SET stage = '{str(new_stage)}' WHERE user_id = '{str(user_id)}'")
            db.commit()

def sub(user_id):
    sql.execute(f"""CREATE TABLE IF NOT EXISTS sub(
    user_id TEXT,
    reg_date TEXT,
    last_activ TEXT
    )""")
    db.commit()
    sql.execute(f"SELECT * FROM sub WHERE user_id = '{str(user_id)}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO sub VALUES ('{str(user_id)}','{str(datetime.datetime.now())[:16]}','{str(datetime.datetime.now())[:16]}')")
        db.commit()
    else:
        sql.execute(f"UPDATE sub SET last_activ = '{str(datetime.datetime.now())[:16]}' WHERE user_id = '{str(user_id)}'")
        db.commit()

def totalSubs():
    sql.execute(f"""CREATE TABLE IF NOT EXISTS sub(
        user_id TEXT,
        reg_date TEXT,
        last_activ TEXT
        )""")
    db.commit()
    num = 0
    sql.execute(f"SELECT * FROM subs")
    for i in sql.fetchall():
        num = num + 1
    return num

def user_balance(user_id, new_balance=None):
    sql.execute(f"""CREATE TABLE IF NOT EXISTS balance(
        user_id TEXT,
        user_balance TEXT
        )""")
    db.commit()
    if new_balance == None:
        sql.execute(f"SELECT * FROM balance WHERE user_id = '{str(user_id)}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO balance VALUES('{str(user_id)}', '0')")
            db.commit()
            return 0
        else:
            to_re = None
            sql.execute(f"SELECT * FROM balance WHERE user_id = '{str(user_id)}'")
            for i in sql.fetchall():
                to_re = i[1]
            return int(to_re)
    elif new_balance != None:
        sql.execute(f"SELECT * FROM balance WHERE user_id = '{str(user_id)}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO balance VALUES('{str(user_id)}', '{str(new_balance)}')")
            db.commit()
        else:
            sql.execute(f"UPDATE balance SET user_balance = '{new_balance}' WHERE user_id = '{str(user_id)}'")
            db.commit()

def back_button(callback_data):
    k = telebot.types.InlineKeyboardButton('Back', callback_data=callback_data)
    return k

def LastPost(post_id, update=False):
    sql.execute(f"""CREATE TABLE IF NOT EXISTS ads(
        user_id TEXT,
        post_id TEXT,
        post_msg TEXT,
        post_media TEXT,
        media_type TEXT,
        last_post TEXT,
        switch TEXT
        )""")
    db.commit()
    if update == False:
        sql.execute(f"SELECT * FROM ads WHERE post_id = '{str(post_id)}'")
        if sql.fetchone() is None:
            return None

        else:
            lp = None
            sql.execute(f"SELECT * FROM ads WHERE post_id = '{str(post_id)}'")
            for i in sql.fetchall():
                lp = i[0]
            return lp

    elif update == True:
        sql.execute(f"SELECT * FROM ads WHERE post_id = '{str(post_id)}'")
        if sql.fetchone() is None:
            return 404
        else:
            sql.execute(f"UPDATE ads SET last_post='{str(datetime.datetime.now())[:16]}' WHERE post_id ='{str(post_id)}'")
            db.commit()

def add_channel(channel_id, admin_id):
    sql.execute(f"""CREATE TABLE IF NOT EXISTS channels(
    channel_id TEXT,
    channel_admin TEXT,
    switch TEXT,
    last_post TEXT
    )""")
    db.commit()
    ch_id = int(channel_id)
    ch_title = bot.get_chat(ch_id).title
    if admin_id == None:
        return 30
    else:
        sql.execute(f"SELECT * FROM channels WHERE  channel_id = '{str(channel_id)}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO channels VALUES('{str(ch_id)}', '{str(admin_id)}', 'False', '----------------')")
            db.commit()
            return 200
        else:
            print('Error! This channel already in use')
            return 103



    



