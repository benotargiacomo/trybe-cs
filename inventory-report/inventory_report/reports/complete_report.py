from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        inventory = 'Produtos estocados por empresa:\n'

        simple_report = SimpleReport.generate(products)

        companies = Counter(
          [product['nome_da_empresa'] for product in products]
        ).most_common()

        for company, qty in companies:
            inventory += f'- {company}: {qty}\n'

        return (
          f'{simple_report}\n'
          f'{inventory}'
        )
