
#### codes ####
200 - OK
103 - Error. Already in use
404 - Error. Not Found
30  - Admin needed

##### functions #####
stages(user_id) = Stage of User. If not exists, create a new one stage with value "None"
stages(user_id, new_stage) = Set a new stage for user. If not exists, create a new one.

sub(user_id) = Update sub last_active. If not exists, create a new subscriber-row

totalSubs() = return num of system subscribers in INTEGER

user_balance(user_id) = return balance of user. If not exists, create a new one row with balance 0
user_balance(user_id, new_balance) = Set a new user-balance. If not exists, add a new one

back_button(callback_data) = return a "back button"

LastPost(post_id) = return Last Post of ad.
LastPost(post_id, update=True) = set a Last Post of ad.


