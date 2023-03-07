from schemas.user import User


class UserController:

    @staticmethod
    def create_user(name: str, birthdate: str, phone: str) -> User: #Se crea user con los argumentos que necesitamos como nombre tipo string, cumpleaños tipo string y telefono tipo string
        user = User(name, birthdate, phone) #Llama a los valores que le mandamos para guardarlos en user
        return user #Regresa la variable de user que creamos arriba
