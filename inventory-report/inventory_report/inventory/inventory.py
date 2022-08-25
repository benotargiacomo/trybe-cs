import csv
import json
import xmltodict
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        if '.csv' in path:
            with open(path, encoding="utf-8") as csv_file:
                data = list(
                  csv.DictReader(csv_file, delimiter=",", quotechar='"')
                )

                return Inventory.generate_report(report_type, data)

        if '.json' in path:
            with open(path) as json_file:
                data = json.load(json_file)

                return Inventory.generate_report(report_type, data)

        if '.xml' in path:
            with open(path, 'r') as xml_file:
                parse = dict(xmltodict.parse(xml_file.read()))
                data = parse['dataset']['record']

                return Inventory.generate_report(report_type, data)

    @staticmethod
    def generate_report(report_type, products):
        if report_type == 'simples':
            return SimpleReport.generate(products)
        elif report_type == 'completo':
            return CompleteReport.generate(products)
        else:
            raise ValueError
