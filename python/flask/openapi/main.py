from marshmallow import Schema, fields


class InputSchema(Schema):
   number = fields.Int(description="Число", required=True, example=5)
   power = fields.Int(description="Степень", required=True, example=2)


class OutputSchema(Schema):
   result = fields.Int(description="Результат", required=True, example=25)


def create_tags(spec):
   """ Создаем теги.

   :param spec: объект APISpec для сохранения тегов
   """
   tags = [{'name': 'math', 'description': 'Математические функции'}]

   for tag in tags:
       print(f"Добавляем тег: {tag['name']}")
       spec.tag(tag)
