
from app import app
from flask import request, redirect
from vviewer.models.samples import Samples


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/samples', methods=['GET', 'POST'])
def getSamples():
    if request.method == 'GET':
        samples = Samples.find_samples()
        return samples
    elif request.method == 'POST':
        data = request.get_json()
        tissue_type = data['tissue_type']
        tumor_sample = data['tumor_sample']
        date_collected = data['date_collected']
        date_used = data['date_used']
        phenotype = data['phenotype'],
        source_id = data['source_id'],
        permissions = data['permissions']
        created_by = data['created_by']
        sample = Samples(tissue_type=tissue_type, source_id=source_id, tumor_sample=tumor_sample, date_collected=date_collected,
                         date_used=date_used, phenotype=phenotype, permissions=permissions, created_by=created_by)
        result = Samples.create_sample(sample)
        return result


@app.route('/samples/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def getSample(id):
    # getting sample
    if request.method == 'GET':
        sample = Samples.find_by_sample_id(id)
        return sample
    elif request.method == 'DELETE':
        response = Samples.delete_sample(id)
        return response
