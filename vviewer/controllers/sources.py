
from app import app
from flask import request, redirect
from vviewer.models.sources import Sources


@app.route('/sources', methods=['GET', 'POST'])
def getSources():
    if request.method == 'GET':
        sources = Sources.find_sources()
        return sources
    elif request.method == 'POST':
        data = request.get_json()
        mrn = data['mrn']
        first_name = data['first_name']
        last_name = data['last_name']
        gender = data['gender']
        dob = data['dob']
        maternal_id = data['maternal_id']
        paternal_id = data['paternal_id']
        family_id = data['family_id']
        permissions = data['permissions']
        created_by = data['created_by']
        source = Sources(mrn=mrn, first_name=first_name, last_name=last_name, gender=gender, dob=dob, maternal_id=maternal_id,
                         paternal_id=paternal_id, family_id=family_id, permissions=permissions, created_by=created_by)
        result = Sources.create_source(source)
        return result


@app.route('/sources/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def getSource(id):
    # getting source
    if request.method == 'GET':
        source = Sources.find_by_source_id(id)
        return source
    elif request.method == 'DELETE':
        response = Sources.delete_source(id)
        return response
