from typing import Dict, Type
from http.client import HTTPSConnection

import orjson
import desert
from marshmallow import Schema

from .base import (
    CollectionGroup,
    BookGroup,
    ChapterGroup,
    Collection,
    Book,
    HadithGroup,
)


class ApiAdaptor:
    def __init__(self, api_key):
        self.key = api_key
        self._schemas: Dict[Type, Schema] = dict()
        self.conn = HTTPSConnection("api.sunnah.com")

    def _get_response(self, endpoint):
        self.conn.request("GET", endpoint, headers={"x-api-key": self.key})
        resp = self.conn.getresponse()
        txt = resp.read().decode("utf8")
        return orjson.loads(txt)

    def _formated_response(self, target_type: Type, endpoint: str, *args, **kwargs):
        if target_type not in self._schemas:
            self._schemas[target_type] = desert.schema(target_type)
        schema = self._schemas[target_type]
        obj = self._get_response(endpoint.format(*args, **kwargs))
        return schema.load(obj)

    def get_collections(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> CollectionGroup:
        return self._formated_response(
            CollectionGroup,
            "/v1/collections?limit={limit}&page={page}",
            page=page,
            limit=limit,
        )

    def get_collection(
        self,
        collection_name: str,
    ) -> Collection:
        return self._formated_response(
            Collection,
            "/v1/collections/{collection_name}",
            collection_name=collection_name,
        )

    def get_books(
        self,
        collection_name: str,
        page: int = 1,
        limit: int = 50,
    ) -> BookGroup:
        return self._formated_response(
            BookGroup,
            "/v1/collections/{collection_name}/books?limit={limit}&page={page}",
            collection_name=collection_name,
            page=page,
            limit=limit,
        )

    def get_book(
        self,
        collection_name: str,
        book_number: int,
    ) -> Book:
        return self._formated_response(
            Book,
            "/v1/collections/{collection_name}/books/{book_number}",
            collection_name=collection_name,
            book_number=book_number,
        )

    def get_chapters(
        self,
        collection_name: str,
        book_number: int,
        page: int = 1,
        limit: int = 50,
    ) -> ChapterGroup:
        return self._formated_response(
            ChapterGroup,
            "/v1/collections/{collection_name}/books/{book_number}/chapters?limit={limit}&page={page}",
            collection_name=collection_name,
            book_number=book_number,
            page=page,
            limit=limit,
        )

    def get_hadiths(
        self,
        collection_name: str,
        book_number: int,
        page: int = 1,
        limit: int = 50,
    ) -> HadithGroup:
        return self._formated_response(
            HadithGroup,
            "/v1/collections/{collection_name}/books/{book_number}/hadiths?limit={limit}&page={page}",
            collection_name=collection_name,
            book_number=book_number,
            page=page,
            limit=limit,
        )


