# coding: utf-8

"""
    SpaceTraders API

    SpaceTraders is an open-universe game and learning platform that offers a set of HTTP endpoints to control a fleet of ships and explore a multiplayer universe.  The API is documented using [OpenAPI](https://github.com/SpaceTradersAPI/api-docs). You can send your first request right here in your browser to check the status of the game server.  ```json http {   \"method\": \"GET\",   \"url\": \"https://api.spacetraders.io/v2\", } ```  Unlike a traditional game, SpaceTraders does not have a first-party client or app to play the game. Instead, you can use the API to build your own client, write a script to automate your ships, or try an app built by the community.  We have a [Discord channel](https://discord.com/invite/jh6zurdWk5) where you can share your projects, ask questions, and get help from other players.   

    The version of the OpenAPI document: 2.0.0
    Contact: joel@spacetraders.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.systems_api import SystemsApi


class TestSystemsApi(unittest.TestCase):
    """SystemsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SystemsApi()

    def tearDown(self) -> None:
        pass

    def test_get_construction(self) -> None:
        """Test case for get_construction

        Get Construction Site
        """
        pass

    def test_get_jump_gate(self) -> None:
        """Test case for get_jump_gate

        Get Jump Gate
        """
        pass

    def test_get_market(self) -> None:
        """Test case for get_market

        Get Market
        """
        pass

    def test_get_shipyard(self) -> None:
        """Test case for get_shipyard

        Get Shipyard
        """
        pass

    def test_get_system(self) -> None:
        """Test case for get_system

        Get System
        """
        pass

    def test_get_system_waypoints(self) -> None:
        """Test case for get_system_waypoints

        List Waypoints in System
        """
        pass

    def test_get_systems(self) -> None:
        """Test case for get_systems

        List Systems
        """
        pass

    def test_get_waypoint(self) -> None:
        """Test case for get_waypoint

        Get Waypoint
        """
        pass

    def test_supply_construction(self) -> None:
        """Test case for supply_construction

        Supply Construction Site
        """
        pass


if __name__ == '__main__':
    unittest.main()