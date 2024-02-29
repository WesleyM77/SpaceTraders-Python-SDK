# coding: utf-8

"""
    SpaceTraders API

    SpaceTraders is an open-universe game and learning platform that offers a set of HTTP endpoints to control a fleet of ships and explore a multiplayer universe.  The API is documented using [OpenAPI](https://github.com/SpaceTradersAPI/api-docs). You can send your first request right here in your browser to check the status of the game server.  ```json http {   \"method\": \"GET\",   \"url\": \"https://api.spacetraders.io/v2\", } ```  Unlike a traditional game, SpaceTraders does not have a first-party client or app to play the game. Instead, you can use the API to build your own client, write a script to automate your ships, or try an app built by the community.  We have a [Discord channel](https://discord.com/invite/jh6zurdWk5) where you can share your projects, ask questions, and get help from other players.   

    The version of the OpenAPI document: 2.0.0
    Contact: joel@spacetraders.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ShipyardTransaction(BaseModel):
    """
    Results of a transaction with a shipyard.
    """ # noqa: E501
    waypoint_symbol: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The symbol of the waypoint.", alias="waypointSymbol")
    ship_symbol: StrictStr = Field(description="The symbol of the ship that was the subject of the transaction.", alias="shipSymbol")
    ship_type: StrictStr = Field(description="The symbol of the ship that was the subject of the transaction.", alias="shipType")
    price: Annotated[int, Field(strict=True, ge=0)] = Field(description="The price of the transaction.")
    agent_symbol: StrictStr = Field(description="The symbol of the agent that made the transaction.", alias="agentSymbol")
    timestamp: datetime = Field(description="The timestamp of the transaction.")
    __properties: ClassVar[List[str]] = ["waypointSymbol", "shipSymbol", "shipType", "price", "agentSymbol", "timestamp"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ShipyardTransaction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShipyardTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "waypointSymbol": obj.get("waypointSymbol"),
            "shipSymbol": obj.get("shipSymbol"),
            "shipType": obj.get("shipType"),
            "price": obj.get("price"),
            "agentSymbol": obj.get("agentSymbol"),
            "timestamp": obj.get("timestamp")
        })
        return _obj

