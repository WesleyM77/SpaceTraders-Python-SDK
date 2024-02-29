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

from pydantic import BaseModel, Field, StrictBool
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from openapi_client.models.faction_symbol import FactionSymbol
from openapi_client.models.faction_trait import FactionTrait
from typing import Optional, Set
from typing_extensions import Self

class Faction(BaseModel):
    """
    Faction details.
    """ # noqa: E501
    symbol: FactionSymbol
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Name of the faction.")
    description: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Description of the faction.")
    headquarters: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The waypoint in which the faction's HQ is located in.")
    traits: List[FactionTrait] = Field(description="List of traits that define this faction.")
    is_recruiting: StrictBool = Field(description="Whether or not the faction is currently recruiting new agents.", alias="isRecruiting")
    __properties: ClassVar[List[str]] = ["symbol", "name", "description", "headquarters", "traits", "isRecruiting"]

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
        """Create an instance of Faction from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in traits (list)
        _items = []
        if self.traits:
            for _item in self.traits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['traits'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Faction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symbol": obj.get("symbol"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "headquarters": obj.get("headquarters"),
            "traits": [FactionTrait.from_dict(_item) for _item in obj["traits"]] if obj.get("traits") is not None else None,
            "isRecruiting": obj.get("isRecruiting")
        })
        return _obj


