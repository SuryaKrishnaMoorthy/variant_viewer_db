"""
Documentation on Uniprot's API:

  https://www.uniprot.org/help/api
"""
import requests


# uniprot URL
URL_UNIPROT = 'https://www.uniprot.org/uniprot/'


def get_prot_seq(protein):
    r = requests.get(URL_UNIPROT + protein)
    return r.content.decode('utf-8')
