from typing import List
from uuid import UUID

from models.todo_model import Todo
from models.user_model import User
from schemas.todo_schema import TodoCreate, TodoUpdate


class TodoService:
     @staticmethod
     async def list_todos(user: User) -> List[Todo]:
        todos = await Todo.find(Todo.owner.id == user.id).to_list()
        return todos
     
     @staticmethod
     async def create_todo(user: User, data: TodoCreate) -> Todo:
          # Se crea una instancia de clase Todo con los datos proporcionados y el propietario del usuario
          # Está creando un nuevo objeto Todo con los datos proporcionados y el propietario del usuario.
          # data.dict() convierte un objeto data en un diccionario. Esto se hace para garantizar que los campos del objeto se puedan pasar como argumentos de palabras clave al constructor de Todo          
          todo = Todo(**data.dict(), owner=user) # **data.dict() está desempaquetando el diccionario en argumentos de palabras clave, para que el constructor de Todo pueda recibirlos como argumentos separados
          return await todo.insert()
     
     
     @staticmethod
     # El parámetro current_user se utiliza para asegurar que el usuario que está haciendo la solicitud de recuperación de la tarea sea el propietario de la tarea
     # Sin este parámetro, cualquier usuario autenticado podría recuperar cualquier tarea de cualquier otro usuario. 
     # En resumen, el uso de current_user ayuda a mantener la seguridad de la aplicación y garantiza que los usuarios solo puedan acceder a los recursos a los que tienen permiso.
     async def retrieve_todo(current_user: User, todo_id: UUID):
        todo = await Todo.find_one(Todo.todo_id == todo_id, Todo.owner.id == current_user.id)
        return todo 
     
     @staticmethod
     # current_user, es el usuario actual que está tratando de actualizar la tarea
     # todo_id, es el ID de la tarea que se va a actualizar
     # data,  es el objeto TodoUpdate que contiene los campos que se van a actualizar en la tarea
     async def update_todo(current_user: User, todo_id: UUID, data: TodoUpdate):
        # buscar la tarea que se va a actualizar. Si la tarea no existe o si el usuario actual no es el propietario de la tarea, se lanzará una excepción
        todo = await TodoService.retrieve_todo(current_user, todo_id)
        # "await todo.update({"$set": data.dict(exclude_unset=True)})" actualiza los campos específicos de un documento en una colección de MongoDB utilizando la operación "$set"
        # El método "dict" de la instancia "data" de la clase "TodoUpdate" devuelve un diccionario que representa los campos y valores actualizados
        # El parámetro "exclude_unset" indica que solo se incluirán en el diccionario los campos que tengan un valor establecido (que no sean None)
        await todo.update({"$set": data.dict(exclude_unset=True)})
        
        await todo.save()
        return todo
    
     @staticmethod
     async def delete_todo(current_user: User, todo_id: UUID) -> None:
        todo = await TodoService.retrieve_todo(current_user, todo_id)
        if todo:
            await todo.delete()
            
        return {"message" : "Successfully removed"}
 