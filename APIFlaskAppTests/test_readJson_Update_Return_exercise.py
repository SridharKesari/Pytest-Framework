import json


def update_user_info(file_name, email, phone):
    with open(file_name, 'r') as f:
        result = json.load(f)
        print(f'\nbefore updating json', result)
        if result['email'] is not None:
            result['email'] = email
        if result['phone'] is not None:
            result['phone'] = phone
        return result


def test_result():
    updated_info = update_user_info('user_exercise.json', 'jane.doe@example.com', '555-5678')
    print(f'after updating json', updated_info)
