import jsonpointer
import json
import jsonvariable


not_found = {
    'a': '$(/b)',
}
try:
    jsonvariable.resolve(not_found)
except jsonvariable.NotFoundError as e:
    print(e)
    print(e.value)
    print(e.pointer)

circular = {
    'a': '$(/b)',
    'b': '$(/a)'
}
try:
    jsonvariable.resolve(circular)
except jsonvariable.CircularReferenceError as e:
    print(e)
    print(e.value)

not_string = {
    'a': 0,
    'b': '$(/a)'
}
try:
    jsonvariable.resolve(not_string)
except jsonvariable.NotStringValueError as e:
    print(e)
    print(e.value)
    print(e.pointer)
    print(e.resolved)
