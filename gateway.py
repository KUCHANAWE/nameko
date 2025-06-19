import eventlet
eventlet.monkey_patch()

from nameko.standalone.rpc import ClusterRpcProxy

config = {'AMQP_URI': "pyamqp://guest:guest@localhost"}

with ClusterRpcProxy(config) as rpc:
    # Contoh penggunaan
    print(rpc.kitchen_service.get_all_tasks())
