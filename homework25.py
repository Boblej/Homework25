class Person:
    def __init__(self, name, age, email):
        self._name = name
        self._age = None
        self._email = email
        self.set_age(age)

    def get_name(self):
        return  self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self._age = age
        else:
            print('возраст должен быть положительным')

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def display(self):
        print(f'name: {self._name}')
        print(f'age: {self._age}')
        print(f'email: {self._email}')

person1 = Person(name="Иван", age=25, email="ivan@example.com")
person1.display()

person1.set_age(-5)

person1.set_email("ivan_new@example.com")
person1.display()
