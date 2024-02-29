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

from openapi_client.models.shipyard_ship import ShipyardShip

class TestShipyardShip(unittest.TestCase):
    """ShipyardShip unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShipyardShip:
        """Test ShipyardShip
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShipyardShip`
        """
        model = ShipyardShip()
        if include_optional:
            return ShipyardShip(
                type = 'SHIP_PROBE',
                name = '',
                description = '',
                supply = 'SCARCE',
                activity = 'WEAK',
                purchase_price = 56,
                frame = openapi_client.models.ship_frame.ShipFrame(
                    symbol = 'FRAME_PROBE', 
                    name = '', 
                    description = '', 
                    condition = 0, 
                    module_slots = 0, 
                    mounting_points = 0, 
                    fuel_capacity = 0, 
                    requirements = openapi_client.models.ship_requirements.ShipRequirements(
                        power = 56, 
                        crew = 56, 
                        slots = 56, ), ),
                reactor = openapi_client.models.ship_reactor.ShipReactor(
                    symbol = 'REACTOR_SOLAR_I', 
                    name = '', 
                    description = '', 
                    condition = 0, 
                    power_output = 1, 
                    requirements = openapi_client.models.ship_requirements.ShipRequirements(
                        power = 56, 
                        crew = 56, 
                        slots = 56, ), ),
                engine = openapi_client.models.ship_engine.ShipEngine(
                    symbol = 'ENGINE_IMPULSE_DRIVE_I', 
                    name = '', 
                    description = '', 
                    condition = 0, 
                    speed = 1, 
                    requirements = openapi_client.models.ship_requirements.ShipRequirements(
                        power = 56, 
                        crew = 56, 
                        slots = 56, ), ),
                modules = [
                    openapi_client.models.ship_module.ShipModule(
                        symbol = 'MODULE_MINERAL_PROCESSOR_I', 
                        capacity = 0, 
                        range = 0, 
                        name = '', 
                        description = '', 
                        requirements = openapi_client.models.ship_requirements.ShipRequirements(
                            power = 56, 
                            crew = 56, 
                            slots = 56, ), )
                    ],
                mounts = [
                    openapi_client.models.ship_mount.ShipMount(
                        symbol = 'MOUNT_GAS_SIPHON_I', 
                        name = '', 
                        description = '', 
                        strength = 0, 
                        deposits = [
                            'QUARTZ_SAND'
                            ], 
                        requirements = openapi_client.models.ship_requirements.ShipRequirements(
                            power = 56, 
                            crew = 56, 
                            slots = 56, ), )
                    ],
                crew = openapi_client.models.shipyard_ship_crew.ShipyardShip_crew(
                    required = 56, 
                    capacity = 56, )
            )
        else:
            return ShipyardShip(
                type = 'SHIP_PROBE',
                name = '',
                description = '',
                supply = 'SCARCE',
                purchase_price = 56,
                frame = openapi_client.models.ship_frame.ShipFrame(
                    symbol = 'FRAME_PROBE', 
                    name = '', 
                    description = '', 
                    condition = 0, 
                    module_slots = 0, 
                    mounting_points = 0, 
                    fuel_capacity = 0, 
                    requirements = openapi_client.models.ship_requirements.ShipRequirements(
                        power = 56, 
                        crew = 56, 
                        slots = 56, ), ),
                reactor = openapi_client.models.ship_reactor.ShipReactor(
                    symbol = 'REACTOR_SOLAR_I', 
                    name = '', 
                    description = '', 
                    condition = 0, 
                    power_output = 1, 
                    requirements = openapi_client.models.ship_requirements.ShipRequirements(
                        power = 56, 
                        crew = 56, 
                        slots = 56, ), ),
                engine = openapi_client.models.ship_engine.ShipEngine(
                    symbol = 'ENGINE_IMPULSE_DRIVE_I', 
                    name = '', 
                    description = '', 
                    condition = 0, 
                    speed = 1, 
                    requirements = openapi_client.models.ship_requirements.ShipRequirements(
                        power = 56, 
                        crew = 56, 
                        slots = 56, ), ),
                modules = [
                    openapi_client.models.ship_module.ShipModule(
                        symbol = 'MODULE_MINERAL_PROCESSOR_I', 
                        capacity = 0, 
                        range = 0, 
                        name = '', 
                        description = '', 
                        requirements = openapi_client.models.ship_requirements.ShipRequirements(
                            power = 56, 
                            crew = 56, 
                            slots = 56, ), )
                    ],
                mounts = [
                    openapi_client.models.ship_mount.ShipMount(
                        symbol = 'MOUNT_GAS_SIPHON_I', 
                        name = '', 
                        description = '', 
                        strength = 0, 
                        deposits = [
                            'QUARTZ_SAND'
                            ], 
                        requirements = openapi_client.models.ship_requirements.ShipRequirements(
                            power = 56, 
                            crew = 56, 
                            slots = 56, ), )
                    ],
                crew = openapi_client.models.shipyard_ship_crew.ShipyardShip_crew(
                    required = 56, 
                    capacity = 56, ),
        )
        """

    def testShipyardShip(self):
        """Test ShipyardShip"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
