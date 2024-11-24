import jsonpath
import json

json_data_str = '{"students": [{"name": "Alice", "age": 20}, {"name": "Bob", "age": 22}]}'
json_data_obj = json.loads(json_data_str)

result = jsonpath.jsonpath(json_data_obj, '$.students[0].name')
print(result)