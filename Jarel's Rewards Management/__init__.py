''' --------MY TDL----------
[Fix the reset order of reward id in class]
every delete
i reset the id order
send the new reward id to be saved

every create
i grab the id from shelve? from class
use that id to make new ones
'''

from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateRewardForm, CreateUserForm
import shelve
import User
import Reward
# from sortedcontainers import SortedDict


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():

        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = User.User(create_user_form.first_name.data,
                         create_user_form.last_name.data,
                         create_user_form.gender.data,
                         create_user_form.membership.data,
                         create_user_form.remarks.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        db.close()

        return redirect(url_for('retrieve_users'))
    return render_template('createUser.html', form=create_user_form)


@app.route('/retrieveUsers')
def retrieve_users():
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)


@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_gender(update_user_form.gender.data)
        user.set_membership(update_user_form.membership.data)
        user.set_remarks(update_user_form.remarks.data)

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_users'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.gender.data = user.get_gender()
        update_user_form.membership.data = user.get_membership()
        update_user_form.remarks.data = user.get_remarks()

        return render_template('updateUser.html', form=update_user_form)


@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
    users_dict = {}
    db = shelve.open('user.db', 'w')
    users_dict = db['Users']

    users_dict.pop(id)

    db['Users'] = users_dict
    db.close()

    return redirect(url_for('retrieve_users'))


# ----------------- Reward Routes ------------------------
@app.route('/createReward', methods=['GET', 'POST'])
def create_reward():
    create_reward_form = CreateRewardForm(request.form)
    if request.method == 'POST' and create_reward_form.validate():

        rewards_dict = {}
        db = shelve.open('reward.db', 'c')

        try:
            rewards_dict = db['Rewards']
        except IOError:
            print("Error in retrieving Rewards from reward.db.")
        except:
            print("Other errors")

        reward = Reward.Reward(create_reward_form.name.data,
                               create_reward_form.desc.data,
                               create_reward_form.points.data,
                               create_reward_form.date.data,
                               create_reward_form.type.data)
        # print(len(rewards_dict))
        # print(reward.get_reward_id())
        rewards_dict[reward.get_reward_id()] = reward
        db['Rewards'] = rewards_dict

        db.close()

        return redirect(url_for('retrieve_rewards'))
    return render_template('createReward.html', form=create_reward_form)


@app.route('/retrieveRewards')
def retrieve_rewards():
    rewards_dict = {}

    try:
        db = shelve.open('reward.db', 'r')
        rewards_dict = db['Rewards']
        db.close()
    except:
        print('No reward.db to read')

    rewards_list = []
    for key in rewards_dict:
        reward = rewards_dict.get(key)
        rewards_list.append(reward)

    return render_template('retrieveRewards.html', count=len(rewards_list), rewards_list=rewards_list)


@app.route('/updateReward/<int:id>/', methods=['GET', 'POST'])
def update_reward(id):
    update_reward_form = CreateRewardForm(request.form)
    if request.method == 'POST' and update_reward_form.validate():
        rewards_dict = {}
        db = shelve.open('reward.db', 'w')
        rewards_dict = db['Rewards']

        reward = rewards_dict.get(id)
        reward.set_name(update_reward_form.name.data)
        reward.set_desc(update_reward_form.desc.data)
        reward.set_points(update_reward_form.points.data)
        reward.set_date(update_reward_form.date.data)
        reward.set_type(update_reward_form.type.data)

        db['Rewards'] = rewards_dict
        db.close()

        return redirect(url_for('retrieve_rewards'))
    else:
        rewards_dict = {}
        db = shelve.open('reward.db', 'r')
        rewards_dict = db['Rewards']
        db.close()

        reward = rewards_dict.get(id)
        update_reward_form.name.data = reward.get_name()
        update_reward_form.desc.data = reward.get_desc()
        update_reward_form.points.data = reward.get_points()
        update_reward_form.date.data = reward.get_date()
        update_reward_form.type.data = reward.get_type()

        return render_template('updateReward.html', form=update_reward_form)


# ----Find the deleted key [working]----
def missing_key(rewards_dict):
    start_key, end_key = list(rewards_dict.keys())[0], list(rewards_dict.keys())[-1]
    find_key = sorted(set(range(start_key, end_key + 1)).difference(rewards_dict))
    return find_key


@app.route('/deleteReward/<int:id>', methods=['POST'])
def delete_reward(id):
    rewards_dict = {}
    db = shelve.open('reward.db', 'w')
    rewards_dict = db['Rewards']

    rewards_dict.pop(id)

    # -------------------------------------test for tdl-----------
    '''
    while len(rewards_dict) != list(rewards_dict.keys())[-1]:
        print("rewards_dict is initially ", rewards_dict)
        print('The current list is ', list(rewards_dict.keys()))
        rewards_dict = SortedDict(rewards_dict)
        print('Missing dict: ', missing_key(rewards_dict))
        print('Missing Key: ', missing_key(rewards_dict)[0])

        # ----Find the next key in sequence and change sequence----
        for_list = missing_key(rewards_dict)[0]  # save the value for code to ref
        rewards_dict[missing_key(rewards_dict)[0]] = rewards_dict[missing_key(rewards_dict)[0]+1]  # replace key
        # print(rewards_dict)
        # print(missing_key(rewards_dict))
        del rewards_dict[for_list+1]  # delete old key[correct]
        print('Before Sort: ', rewards_dict)
        rewards_dict = SortedDict(rewards_dict)  # Sort rewards_dict
        print(rewards_dict)
    '''
    # ------------------------------------------------------------

    db['Rewards'] = rewards_dict
    db.close()

    return redirect(url_for('retrieve_rewards'))


if __name__ == '__main__':
    app.run()
