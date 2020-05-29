#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date      : 2020-05-27 12:01
# Author    : Mr.He
# Usage     : 
# Version   :
# Comment   :


# Import built-in modules
import os
# Import third-party modules

# Import local modules
from NodeGraphQt import BaseNode


class MoreIconNode(BaseNode):
    """
    more icon node
    """

    __identifier__ = 'More'
    NODE_NAME = 'Icon'

    def __init__(self):
        super(MoreIconNode, self).__init__()
        self._input_port = self.add_input("image_path", display_name=False)
        self.add_icon_label('icon path', icon_path=r"", tab='widgets')

    def set_pixmap(self, icon_path):
        self.get_widget("icon path").value = icon_path
        self.set_property("icon path", icon_path)

    def run(self):
        input_node = self._input_port.connected_ports()[0].node()
        path = input_node.get_property("out")
        if path:
            path = path.replace("\\", "/")
            if os.path.isfile(path):
                self.set_pixmap(path)

    def on_input_connected(self, to_port, from_port):
        self.run()

    def on_input_disconnected(self, in_port, out_port):
        self.set_pixmap("")


class MoreTextNode(BaseNode):
    """
    More user node
    """

    __identifier__ = 'More'
    NODE_NAME = 'Text'

    def __init__(self):
        super(MoreTextNode, self).__init__()
        self.add_output('out')
        self.add_text_input('out', 'More Text', text='', tab='widgets', multi_line=True)
        self.get_widget("out").value_changed.connect(self.update_stream)


class MoreBrowserFileNode(BaseNode):
    """
    More user node
    """

    __identifier__ = 'More'
    NODE_NAME = 'Browser File'

    def __init__(self):
        super(MoreBrowserFileNode, self).__init__()
        self.add_output('out')
        self.add_file_input('out', 'Browser File', text='', tab='widgets')
        self.get_widget("out").value_changed.connect(self.update_stream)


class MoreTaskNode(BaseNode):
    """
    More Task Node
    """
    __identifier__ = 'More'
    NODE_NAME = 'Task'

    def __init__(self):
        super(MoreTaskNode, self).__init__()

        self._output_port_name = "out"

        self.user_input_port = self.add_input("user_input")
        self.add_output(self._output_port_name)

    def run(self):
        user_node = self.user_input_port.connected_ports()[0].node()
        user_name = user_node.get_property("out")

        self.set_property("user_name", user_name)

        task = "{}.tasks".format(user_name)
        self.set_property(self._output_port_name, task)

    def on_input_connected(self, to_port, from_port):
        """Override node callback method."""
        self.run()
        self.update_stream()

    def on_input_disconnected(self, to_port, from_port):
        """Override node callback method."""
        self.set_property(self._output_port_name, None)
        self.update_stream()
