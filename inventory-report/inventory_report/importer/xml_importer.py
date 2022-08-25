from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if '.xml' not in path:
            raise ValueError('Arquivo inválido')
        with open(path, 'r') as file:
            parse = dict(xmltodict.parse(file.read()))
            data = parse['dataset']['record']

            return data
