from collections import Counter
from datetime import date


class SimpleReport:
    @staticmethod
    def generate(products):
        today = date.today().isoformat()

        oldest_date = min(
          [product['data_de_fabricacao'] for product in products]
        )

        closest_date = min([product['data_de_validade']
                            for product in products
                            if product['data_de_validade'] > today
                            ])

        most_common_company = Counter(
          [product['nome_da_empresa'] for product in products]
        ).most_common(1)[0][0]

        return (
          f'Data de fabricação mais antiga: {oldest_date}\n'
          f'Data de validade mais próxima: {closest_date}\n'
          f'Empresa com mais produtos: {most_common_company}'
        )
