from flask import jsonify
from pocketbase import PocketBase

pb = PocketBase('http://127.0.0.1:8090')


def create_clan(username, clan_name):
    data = {
        "name": clan_name,
        "members": [username],
        "curr_xp": 0,
        "target_xp": 10,
    }
    try:
        # Check if the clan name already exists
        existing_clan = pb.collection("clans").get_first_list_item(f'name="{clan_name}"')

        if existing_clan:
            return {'error': 'Clan name already taken'}, 400

        # Create the new clan
        new_clan = pb.collection("clans").create(data)
        return {'message': f'Clan {data["name"]} created successfully with ID {new_clan["id"]}'}, 200
    except Exception as e:
        return {'error': str(e)}, 500


def leave_clan(username, clan_name):
    pass


def join_clan(username, clan_name):
    try:
        user = pb.collection("users").get_first_list_item(f'username="{username}"')
        if not user:
            return {'error': 'User not found'}, 404
        clan = pb.collection("clans").get_first_list_item(f'name="{clan_name}"')
        if not clan:
            return {'error': 'Clan not found'}, 404
        members = clan.get('members', [])
        if user['id'] in members:
            return {'error': 'User is already a member of the clan'}, 400

        members.append(user['id'])
        updated_clan = pb.collection("clans").update(clan['id'], {'members': members})

        return {'message': f'User {username} added to clan {clan_name} successfully'}, 200
    except Exception as e:
        return {'error': str(e)}, 500


def clan_level_up(add_xp, clan_name):
    clan = pb.collection("clans").get_first_list_item(f'name="{clan_name}"')
    if not clan:
        return {'error': 'Clan not found'}, 404
    
    # Calculate new XP
    new_xp = clan['xp'] + add_xp
    
    if new_xp >= clan['target_xp']:
        # Update XP and target XP
        new_target_xp = clan['target_xp'] * 1.5
        pb.collection("clans").update(clan['id'], {'xp': new_xp, 'target_xp': new_target_xp})
    else:
        # Just update the XP
        pb.collection("clans").update(clan['id'], {'xp': new_xp})
    
    return {'message': f'Clan {clan_name} updated successfully'}, 200


def _clan_stats():
    ret = pb.collection('clans').get_first_list_item('name="CSESOC"')
    total_weight = 100
    print(ret.name)
    # for member in ret['members']:
    #     total_weight += pb.collection('users').get_first_list_item(f'id={member['id']}')

    # due to time constraints, return default values
    default_level = 10
    default_rewards = 24
    ret_dic = {
        "name": ret.name,
        "num_members": len(ret.members),
        "level": ret.level,
        'weight_lifted': total_weight,
        'curr_xp': ret.curr_xp,
        'target_xp': ret.target_xp,
    }

    return ret_dic


def clan_list_all():
    pass
