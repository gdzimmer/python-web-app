from flask import jsonify, request, abort

from data_service import DataService

DATA_PROVIDER = DataService()

people_info = [{'name': 'Jo Bloggs', 'age': '32', 'occupation': 'Engineer'},
               {'name': 'Jake Bloggs', 'age': '31', 'occupation': 'Builder'}]

def index():
    """this is a loading page"""
    # This is a comment
    return 'Hello World'

def db():
    return 'Hello Grads'

def user_profile(id):
    return "Profile page of user #{}".format(id)

def person():
    return jsonify(people_info)

def person_add():
    try:
        data = request.get_json(force=True)
        name = data['name']
        age = data['age']
        occupation = data['occupation']
        if name and age and occupation:
            people_info.append({'name': name, 'age': age, 'occupation': occupation})
            return jsonify({"Person " + name: "Added successfully"})
    except Exception as exc:
        print(exc)
        abort(400)

def person_update():
    try:
        # retrieve name and check if in dictionary
        data = request.get_json(force=True)
        name = data['name']
        age = data['age']
        occupation = data['occupation']

        person_to_update = None
        # if user exists update with the given information
        if name and age and occupation:
            for index, person in enumerate(people_info):
                print(person)
                if person['name'] == name:
                    person_to_update = person
            if person_to_update is not None:
                person_to_update['age'] = age
                person_to_update['occupation'] = occupation
                return jsonify({"Person " + name: "Updated successfully"})
            else:
                return jsonify({"Person " + name: "Updated Failed"}), 404

    # if failed
    except Exception as exc:
        print(exc)
        abort(404)

def person_delete():
    try:
        # retrieve name and check if in dictionary
        data = request.get_json(force=True)
        name = data['name']
        person_to_delete = None

        # if user exists find them and remove
        if name:
            for index, person in enumerate(people_info):
                print(index, person)
                if person['name'] == name:
                    person_to_delete = person
            if person_to_delete is not None:
                people_info.remove(person_to_delete)
                return jsonify({"Person " + name: "Deleted successfully"})
            else:
                return jsonify({"Person " + name: "Not Deleted"}), 404

    # if failed
    except Exception as exc:
        print(exc)
        abort(404)


def read_widgets():
    widgets = DATA_PROVIDER.get_widget()
    widgets_dict = {}
    for widget in widgets:
        widgets_dict[widget[0]]={'Name':widget[1], 'Price': str(widget[2])}
    return jsonify(widgets_dict)

def read_widget_by_id(widget_id):
    db_widget = DATA_PROVIDER.get_widget(widget_id)
    if db_widget:
        widget = {'ID': widget_id, 'Name': db_widget[1], 'Price': str(db_widget[2])}
        return jsonify(widget)
    else:
        abort(404)