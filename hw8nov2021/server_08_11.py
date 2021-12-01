import json
from copy import deepcopy

from flask import Blueprint,  request, abort, render_template
from flask import Response
from .models import *

bp = Blueprint('person', __name__)

@bp.route('/', methods=['GET', 'POST'])
def person_list():
    if request.method == 'GET':

        data = [Person('asdf', 'asdf', 23), Person('AAAAA', 'KKMNB', 48)]

        tmp_list = []
        for person in data:
            tmp_list.append(str(person))
        return json.dumps(tmp_list)



@bp.route('/<int:person_id>')
def person_detail(person_id):
    for person in Person.list_per:
        if person.id == person_id:
            return person.to_json()
    else:
        abort(404)