from marshmallow import Schema, fields
from marshmallow.validate import Range, Length

class ReviewSchema(Schema):
    company_name = fields.Str(validate=Length(2, 150))
    city = fields.Str(validate=Length(0, 150))
    phone = fields.Int(validate=Range(0, 11))

REVIEW_SCHEMA = {
    '$schema': 'http://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'company_name':
            {'type': 'string',
             'max_lenght': 150,
             },
        'city':
            {'type': 'string',
             'max_lenght': 150},
        'phone':
            {'type': 'integer',
             'min_lenght': 11,
             'max_lenght': 11
             },
    },
    'required': ['company_name'],
}