from __future__ import annotations

from typing import List

from pydantic import BaseModel, RootModel


class PriceHistoryItem(BaseModel):
    x: int
    y: int


class Days(BaseModel):
    days: int
    max_price: float
    min_price: float
    up_times: int
    down_times: int
    last_continue_times: int
    last_increase_status: bool


class Statistics(BaseModel):
    days730: Days | None = None
    days365: Days | None = None
    days180: Days | None = None
    days90: Days | None = None
    days30: Days | None = None
    days7: Days | None = None


class PriceHistoryAttributes(BaseModel):
    symbol: str
    currency: str
    # nindex: str
    # oid: str
    current_price: float
    # datetime_format: str
    # price_history: List[PriceHistoryItem]
    # purl: str | None = None
    url: str | None = None
    title: str
    nindex_name: str
    # icon: str
    statistics: Statistics
    state: str


class PriceHistoryAPIRet(RootModel):
    root: dict[str, PriceHistoryAttributes]
