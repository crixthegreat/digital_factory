#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/7/29 11:44:30

from digital_factory import const as const

class Factory_Node():

    def __init__(self, node_id, sub_node_list):

        self.id = node_id
        self.sub_node = sub_node_list
        self.status = const.Node_STATUS['OFF_LINE']
