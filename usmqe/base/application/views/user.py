from widgetastic.widget import Text, TextInput, Table
# from widgetastic.exceptions import NoSuchElementException
# from widgetastic.widget import GenericLocatorWidget, ParametrizedLocator, ParametrizedView

from usmqe.base.application.views.common import BaseLoggedInView
from usmqe.base.application.widgets import Kebab
from taretto.ui.patternfly import Button, Dropdown


class UsersView(BaseLoggedInView):
    """
    View for Users page. Available to admin only
    """
    # TODO: fix dropdown. If clicked, dropdown changes its name and won't be found anymore
    pagename = Text(".//h1")
    filter_type = Dropdown("User ID")
    user_filter = TextInput(placeholder='Filter by User ID')
    adduser = Button("Add")
    users = Table(".//table", column_widgets={5: Button("Edit"), 6: Kebab()})

    @property
    def is_displayed(self):
        return self.pagename.text == "Users"
