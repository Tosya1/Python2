# 5.Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.
# 6.Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.


class Animal:
    def __init__(self, name: str, weight: int, age: int, gender: str):
        self.name = name
        self.gender = gender
        self.weight = weight
        self.age = age

    def move(self):
        pass

    def say(self):
        pass

    def __str__(self) -> str:
        return f'Имя: {self.name}, Пол: {self.gender}, Возраст: {self.age}, Вес: {self.weight}'


class Bird(Animal):
    def __init__(self, name: str, weight: int, age: int, gender: str, bird_type: str):
        self.bird_type = bird_type
        super().__init__(name, weight, age, gender)

    def move(self) -> str:
        return 'Летать'

    def say(self) -> str:
        return 'Чирик'

    def __str__(self) -> str:
        return f'{super().__str__()}, Вид: {self.bird_type}'


class Dog(Animal):
    def __init__(self, name: str, weight: int, age: int, gender: str, dog_type: str):
        self.dog_type = dog_type
        super().__init__(name, weight, age, gender)

    def move(self) -> str:
        return 'Бегать'

    def say(self) -> str:
        return 'Гав'

    def __str__(self) -> str:
        return f'{super().__str__()}, Порода: {self.dog_type}'


class Fish(Animal):
    def __init__(self, name: str, weight: int, age: int, gender: str, fish_type: int):
        self.fish_type = fish_type
        super().__init__(name, weight, age, gender)

    def move(self) -> str:
        return 'Плавать'

    def __str__(self) -> str:
        return f'{super().__str__()} Вид: {self.fish_type}'


class AnimalFactory():
    animal_types: dict[str, type] = {
        i.__name__: i for i in Animal.__subclasses__()}

    def __init__(self, animal_type: str, *args, **kwargs):
        self.animal_type = animal_type
        self.animal = AnimalFactory.animal_types[self.animal_type](
            *args, **kwargs)

    def get_animal(self):
        return self.animal

    def __str__(self) -> str:
        return f'Класс: {self.animal_type}, {self.animal} '


if __name__ == '__main__':

    animal1 = AnimalFactory('Bird', 'Гоша', 1, 1, 'м', 'Попугай')
    animal2 = AnimalFactory('Fish', 'Федя', 5, 2, 'м', 'Речной')
    animal3 = AnimalFactory('Dog', 'Рекс', 15, 3, 'м', 'Овчарка')

    print(animal1, animal2, animal3, sep='\n')
    print(f'{animal1.get_animal()}, Класс: {type(animal1.get_animal())}',
          f'{animal2.get_animal()}, Класс: {type(animal2.get_animal())}',
          f'{animal3.get_animal()}, Класс: {type(animal3.get_animal())}', sep='\n')
