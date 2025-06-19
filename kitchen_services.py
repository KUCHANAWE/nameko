from nameko.rpc import rpc
from depedencies import Database

class KitchenService:
    name = "kitchen_service"
    db = Database()

    @rpc
    def get_all_tasks(self):
        return self.db.query("SELECT * FROM kitchen_tasks")

    @rpc
    def get_task_by_id(self, task_id):
        result = self.db.query("SELECT * FROM kitchen_tasks WHERE kitchen_task_id = %s", (task_id,))
        return result[0] if result else None

    @rpc
    def get_tasks_by_chef(self, chef_name):
        return self.db.query("SELECT * FROM kitchen_tasks WHERE chef = %s", (chef_name,))

    @rpc
    def create_task(self, kitchen_id, menu, quantity, chef=None, notes=None):
        return self.db.execute("""
            INSERT INTO kitchen_tasks (kitchen_id, menu, quantity, chef, status, notes, created_at, updated_at)
            VALUES (%s, %s, %s, %s, 'pending', %s, NOW(), NOW())
        """, (kitchen_id, menu, quantity, chef, notes))

    @rpc
    def update_task(self, task_id, status=None, notes=None):
        # Update status dan/atau notes jika disediakan
        updates = []
        params = []
        if status:
            updates.append("status = %s")
            params.append(status)
        if notes:
            updates.append("notes = %s")
            params.append(notes)
        if not updates:
            return False
        updates.append("updated_at = NOW()")
        sql = f"UPDATE kitchen_tasks SET {', '.join(updates)} WHERE kitchen_task_id = %s"
        params.append(task_id)
        self.db.execute(sql, tuple(params))
        return True

    @rpc
    def delete_task(self, task_id):
        self.db.execute("DELETE FROM kitchen_tasks WHERE kitchen_task_id = %s", (task_id,))
        return True
