from marshmallow.fields import String

from admin.models import SQLAlchemySchema, Schema, ma
from geomex.models import Neighborhood, Municipality, State


class NeighborhoodSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Neighborhood
        fields = (
            Neighborhood.id.key,
            Neighborhood.name.key,
        )


class MunicipalitySchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Municipality
        fields = (
            Municipality.id.key,
            Municipality.name.key,
        )


class StateSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = State
        fields = (
            State.id.key,
            State.name.key
        )


class GeomexSchema(Schema):
    postal_code = String()
    neighborhoods = ma.Nested(NeighborhoodSchema, many=True)
    municipality = ma.Nested(MunicipalitySchema)
    state = ma.Nested(MunicipalitySchema)


class PostCodeArgs(Schema):
    postcode = String(required=True)