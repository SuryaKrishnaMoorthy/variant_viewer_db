
from app import app
from flask import request, redirect
from vviewer.models.studies import Studies


@app.route('/studies', methods=['GET', 'POST'])
def getStudies():
    if request.method == 'GET':
        studies = Studies.find_studies()
        return studies
    elif request.method == 'POST':
        data = request.get_json()
        source_id = data['source_id'],
        permissions = data['permissions']
        study = Studies(permissions=permissions, source_id=source_id)
        result = Studies.create_study(study)
        return result


@app.route('/study/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def getStudy(id):
    # getting source
    if request.method == 'GET':
        study = Studies.find_by_study_id(id)
        return study
