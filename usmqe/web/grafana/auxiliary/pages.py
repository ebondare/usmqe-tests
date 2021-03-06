"""
Some usefull methods and classes for common work with Grafana
"""


from webstr.core import WebstrPage
from webstr.common.dialogs.pages import OkCancelDlg

import usmqe.web.grafana.auxiliary.models as m_auxiliary
from usmqe.web.grafana.exceptions import ValueNotFoundError


class GenericDropDownList(WebstrPage):
    """
    auxiliary class for Charts
    """
    _model = m_auxiliary.GenericDropDownListModel
    _label = 'drop down list'
    _required_elems = ['_root']

    @property
    def value(self):
        """ returns selected value """
        return self._model._root.text

    @value.setter
    def value(self, required_value):
        """
        Select value in the list

        Parameters:
            required_value (string): value in the dropdown list
        """
        self._model._root.click()
        found = False
        for row in self._model.rows:
            if row.text == required_value:
                found = True
                row.click()
                break
        if not found:
            raise ValueNotFoundError(
                'Cluster {} not found'.format(required_value))


class GenericChart(WebstrPage):
    """
    auxiliary class for Charts
    """
    _model = m_auxiliary.GenericChartModel
    _label = 'generic chart'
    _required_elems = ['header']

    def click_on_export_csv(self):
        """
        click on export_csv link, which is hidden in extended menu
        """
        self._model.header.click()
        self._model.extended_menu.click()
        self._model.export_csv.click()

    def export_csv(self, as_rows=True, time_format=None):
        """
        export grafana chart data to csv file

        Parameters:
            as_rows (boolean): choose mode
                               'Series as rows' if True or
                               'Series as columns' when False
                               it is True by default
            time_format (string): time format string
        """
        self.click_on_export_csv()
        export_window = ExportDialog()
        if not as_rows:
            export_window.mode.value = 'Series as columns'
        if time_format is not None:
            export_window.time_format.value = time_format
        export_window.submit()


class ExportDialog(OkCancelDlg):
    """
    Export to csv file dialog
    """
    _model = m_auxiliary.ExportDialogModel
    _label = 'export to csv file dialog'

    @property
    def mode(self):
        """
        returns selected mode
        """
        return self._model.mode.value

    @mode.setter
    def mode(self, value):
        """
        set mode
        """
        self._model.mode.value = value

    @property
    def time_format(self):
        """
        returns selected time_format
        """
        return self._model.time_format.value

    @time_format.setter
    def time_format(self, value):
        """
        set time_format
        """
        self._model.time_format.value = value


class SingleStat(WebstrPage):
    """
    auxiliary class for Single Stat panels
    """
    _model = m_auxiliary.SingleStatModel
    _label = 'single stat'
    _required_elems = ['header', 'value']

    @property
    def value(self):
        """
        returns value in the panel
        """
        return self._model.value.text
