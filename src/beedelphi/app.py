"""
IDE for Python learners
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class BeeDelphiIDE(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        left_content = toga.Box(
            style=Pack(direction=COLUMN, width=150) # , padding_top=50)
        )
        left_content.add(toga.Label('Left Column'))
        left_container = toga.ScrollContainer(horizontal=False)
        left_container.content = left_content

        center_content = toga.Box(
            style=Pack(direction=COLUMN) # , padding_top=50)
        )
        center_content.add(toga.Label('Center Column'))
        center_container = toga.ScrollContainer(horizontal=False)
        center_container.content = center_content

        right_content = toga.Box(
            style=Pack(direction=COLUMN, width=150) # , padding_top=50)
        )
        right_content.add(toga.Label('Right Column'))
        right_container = toga.ScrollContainer(horizontal=False)
        right_container.content = right_content

        split = toga.SplitContainer()

        split.content = [left_container, center_container, right_container]

        main_box = toga.Box(children=[split], style=Pack(direction=COLUMN))

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return BeeDelphiIDE()
