from strawberry.fastapi import GraphQLRouter
from .esquema import schema

router = GraphQLRouter(schema)