#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/7/29 11:47:12

import digital_factory.factory_node as node

class Factory(node.Factory_Node):

    def __init__(self, node_id, sub_node=None):
        super().__init__(node_id, sub_node)

    def run(self):
        print('The factory: {} is running'.format(self.id))
        print('The status of factory is: {}'.format(self.status))
