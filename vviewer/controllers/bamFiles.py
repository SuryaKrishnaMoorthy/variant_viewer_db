
from app import app
from flask import request, redirect
from vviewer.models.bamFiles import BamFiles


@app.route('/bamFiles', methods=['GET', 'POST'])
def getbamFiles():
    if request.method == 'GET':
        bamFiles = BamFiles.find_bamFiles()
        return bamFiles
    elif request.method == 'POST':
        data = request.get_json()
        original_filename = data['original_filename']
        file_path = data['file_path']
        date_sequenced = data['date_sequenced']
        sequencer = data['sequencer']
        sample_id = data['sample_id']
        sequence_integer_id = data['sequence_integer_id'],
        read_group = data['read_group'],
        permissions = data['permissions']
        created_by = data['created_by']
        created_on = data['created_on']
        bamFile = BamFiles(original_filename=original_filename, file_path=file_path, date_sequenced=date_sequenced,
                           sequencer=sequencer, sample_id=sample_id, sequence_integer_id=sequence_integer_id,
                           read_group=read_group, permissions=permissions, created_by=created_by, created_on=created_on)
        result = BamFiles.create_bamFile(bamFile)
        return result


@app.route('/bamFiles/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def getBamFiles(id):
    # getting sample
    if request.method == 'GET':
        bamFile = BamFiles.find_by_bamFile_id(id)
        return bamFile
    elif request.method == 'DELETE':
        response = BamFiles.delete_bamFile(id)
        return response
