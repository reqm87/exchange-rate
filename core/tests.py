from serializer import banxico_format, dof_format, fixer_format
from tests_banxico_data import banxico_input, banxico_output
from tests_dof_data import dof_input, dof_output
from tests_fixer_data import fixer_input, fixer_output


class TestExchangeRate(object):
    def test_dof_serializer(self):
        data = dof_format(dof_input)
        assert data['dof']['value'] == dof_output['dof']['value']

    def test_fixer_serializer(self):
        data = fixer_format(fixer_input)
        assert data['fixer']['value'] == fixer_output['fixer']['value']

    def test_banxico_serializer(self):
        data = banxico_format(banxico_input)
        assert data['banxico']['value'] == banxico_output['banxico']['value']
