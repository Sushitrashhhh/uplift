from flask import jsonify
from pocketbase import PocketBase

pb = PocketBase('http://127.0.0.1:8090')


def create_user(username, email, password):
    data = {
        "username": username,
        "email": email,
        "emailVisibility": True,
        "password": password,
        "passwordConfirm": password,
        "name": "test_name",
        "curr_xp": 123,
        "target_xp": 123
    }
    print("CREATING USER WITH THE DATA:", data)
 
    try:
        user = pb.collection("users").create(data)
        return {'message': f'User {data["username"]} created successfully with ID {user.id}'}, 200
    except Exception as e:
        print(f"Error creating user: {str(e)}")  # Print the error to the console for debugging
        return {'error': str(e)}, 500


def user_level_up(username, level):
    pass


def user_stat(user_id):
    # user = pb.collection("users").get_first_list_item(f'id={user_id}')
    #
    # if not user:
    #     raise Exception
    #
    # print(user)
    #
    # user_data = user['items'][0]

    # return user_data

    return {'username': "hi"}
