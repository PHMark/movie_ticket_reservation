from marshmallow import Schema, fields


class SeatSchema(Schema):
    """Use to represent the SeatModel as JSON data."""

    id = fields.Int()
    row_id = fields.Int()
    row_letter = fields.String()
    row_letter_id = fields.Int()
