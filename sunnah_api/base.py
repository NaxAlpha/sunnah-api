from enum import Enum
from typing import List, Union
from dataclasses import dataclass
from functools import cached_property

# --------------------------------------------------------------
# Basic things
# --------------------------------------------------------------


def get_prop(self, attr, lang):
    for elem in getattr(self, attr):
        if elem.lang == lang:
            return elem
    return None


class LangInfo(Enum):
    ar = "ar"
    en = "en"


@dataclass
class _Lang:
    lang: LangInfo


@dataclass
class _BaseApiResult:
    total: int
    limit: int
    previous: Union[int, None]
    next: Union[int, None]


# --------------------------------------------------------------
# Collection related types
# --------------------------------------------------------------


@dataclass
class CollectionInfo(_Lang):
    title: str
    shortIntro: str


@dataclass
class Collection:
    name: str
    hasBooks: bool
    hasChapters: bool
    collection: List[CollectionInfo]
    totalHadith: int
    totalAvailableHadith: int

    @cached_property
    def en_collection(self) -> CollectionInfo:
        return get_prop(self, "collection", LangInfo.en)

    @cached_property
    def ar_collection(self) -> CollectionInfo:
        return get_prop(self, "collection", LangInfo.ar)


@dataclass
class CollectionGroup(_BaseApiResult):
    data: List[Collection]


# --------------------------------------------------------------
# Book related types
# --------------------------------------------------------------


@dataclass
class BookInfo(_Lang):
    name: str


@dataclass
class Book:
    bookNumber: Union[int, str]
    book: List[BookInfo]
    hadithStartNumber: int
    hadithEndNumber: int
    numberOfHadith: int

    @cached_property
    def en_book(self) -> BookInfo:
        return get_prop(self, "book", LangInfo.en)

    @cached_property
    def ar_book(self) -> BookInfo:
        return get_prop(self, "book", LangInfo.ar)


@dataclass
class BookGroup(_BaseApiResult):
    data: List[Book]


# --------------------------------------------------------------
# Chapter related types
# --------------------------------------------------------------


@dataclass
class ChapterInfo(_Lang):
    chapterNumber: int
    chapterTitle: str
    intro: Union[str, None]
    ending: Union[str, None]


@dataclass
class Chapter:
    bookNumber: int
    chapterId: float
    chapter: List[ChapterInfo]


@dataclass
class ChapterGroup(_BaseApiResult):
    data: List[Chapter]


# --------------------------------------------------------------
# Hadith related types
# --------------------------------------------------------------


@dataclass
class HadithGrade:
    graded_by: Union[str, None]
    grade: str


@dataclass
class HadithInfo(_Lang):
    chapterNumber: int
    chapterTitle: str
    urn: int
    body: str
    grades: List[HadithGrade]


@dataclass
class Hadith:
    collection: str
    bookNumber: int
    chapterId: float
    hadithNumber: int
    hadith: List[HadithInfo]

    @cached_property
    def en_hadith(self) -> HadithInfo:
        return get_prop(self, "hadith", LangInfo.en)

    @cached_property
    def ar_hadith(self) -> HadithInfo:
        return get_prop(self, "hadith", LangInfo.ar)


@dataclass
class HadithGroup(_BaseApiResult):
    data: List[Hadith]
