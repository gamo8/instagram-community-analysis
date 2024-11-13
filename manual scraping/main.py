import base64
import json
import re
import os


def extract_profile(data):
    return data['data']['user']

def extract_followings(data):
    friendship_api_url = "https://www.instagram.com/api/v1/friendships/.*/following/"
    contents = [entry['response']['content'] for entry in data['log']['entries']
        if re.match(friendship_api_url, entry['request']['url'])]
    
    users = []
    for content in contents:
        if 'text' not in content:
            continue
        text = content['text']

        if 'encoding' in content:
            if content['encoding'] == 'base64':
                text = base64.b64decode(text).decode('utf-8')
                user_json = json.loads(text)
                users.extend(user_json['users'])
        else:
            user_json = json.loads(text)
            users.extend(user_json['users'])

    return users

def extract_person(person):

    followings_path = f'./data/{person}/followings.har'
    profile_path = f'./data/{person}/profile.json'
    print(followings_path)
    print(profile_path)


    with open(f'./data/{person}/followings.har', 'r') as f:
        data = json.loads(f.read())
        followings = extract_followings(data)


    with open(f'./data/{person}/profile.json', 'r') as f:
        data = json.loads(f.read())
        profile = extract_profile(data)
            
    output = {
        'general': profile,
        'followings': followings
    }

    return output, profile['id']

   
def extract_all():
    persons = os.listdir('./data')

    users = {}
    for person in persons:
        output, id = extract_person(person)
        users[id] = output
    with open('./out/people.json', 'w') as f:
        f.write(json.dumps(users))

extract_all()