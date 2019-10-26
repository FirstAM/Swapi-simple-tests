import json
import pytest
from src.request_helper import RequestHelper


class SchemeHelper:
    types = {"string": "str", "array": "list", "integer": "int", "object": "dict"}
    schema = RequestHelper().get_schema().json()

    def get_resource_format(self, resource):
        properties = self.schema['properties']
        try:
            type_resource = properties[resource]['type']
        except KeyError:
            print("Ops ! Wrong resource")
            type_resource = "title"

        for type in self.types:
            if type == type_resource:
                return self.types[type]
