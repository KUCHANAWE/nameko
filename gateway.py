import eventlet
eventlet.monkey_patch()

from nameko.web.handlers import http
from nameko.rpc import RpcProxy
import json

from datetime import datetime

def serialize(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return obj

class KitchenGatewayService:
    name = "gateway"

    kitchen_rpc = RpcProxy("kitchen_service")

    @http('GET', '/tasks')
    def get_all_tasks(self, request):
        try:
            data = self.kitchen_rpc.get_all_tasks()
            return 200, json.dumps({"data": data}, default=serialize)
        except Exception as e:
            return 500, json.dumps({"error": str(e)}, default=serialize)

    @http('GET', '/tasks/<int:task_id>')
    def get_task_by_id(self, request, task_id):
        try:
            data = self.kitchen_rpc.get_task_by_id(task_id)
            if data:
                return 200, json.dumps({"data": data}, default=serialize)
            return 404, json.dumps({"error": "Task not found"})
        except Exception as e:
            return 500, json.dumps({"error": str(e)}, default=serialize)

    @http('GET', '/tasks/chef/<string:chef>')
    def get_tasks_by_chef(self, request, chef):
        try:
            data = self.kitchen_rpc.get_tasks_by_chef(chef)
            return 200, json.dumps({"data": data}, default=serialize)
        except Exception as e:
            return 500, json.dumps({"error": str(e)}, default=serialize)

    @http('POST', '/tasks')
    def create_task(self, request):
        try:
            body = json.loads(request.get_data(as_text=True))
            kitchen_id = body["kitchen_id"]
            menu = body["menu"]
            quantity = body["quantity"]
            chef = body.get("chef")
            notes = body.get("notes")
            task_id = self.kitchen_rpc.create_task(kitchen_id, menu, quantity, chef, notes)
            return 201, json.dumps({"message": "Task created", "task_id": task_id})
        except KeyError as e:
            return 400, json.dumps({"error": f"Missing field: {str(e)}"})
        except Exception as e:
            return 500, json.dumps({"error": str(e)}, default=serialize)

    @http('PUT', '/tasks/<int:task_id>')
    def update_task(self, request, task_id):
        try:
            body = json.loads(request.get_data(as_text=True))
            status = body.get("status")
            notes = body.get("notes")
            success = self.kitchen_rpc.update_task(task_id, status, notes)
            if success:
                return 200, json.dumps({"message": "Task updated"})
            return 400, json.dumps({"error": "Nothing to update"})
        except Exception as e:
            return 500, json.dumps({"error": str(e)}, default=serialize)

    @http('DELETE', '/tasks/<int:task_id>')
    def delete_task(self, request, task_id):
        try:
            self.kitchen_rpc.delete_task(task_id)
            return 200, json.dumps({"message": "Task deleted"})
        except Exception as e:
            return 500, json.dumps({"error": str(e)}, default=serialize)
