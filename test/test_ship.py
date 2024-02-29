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

from openapi_client.models.ship import Ship

class TestShip(unittest.TestCase):
    """Ship unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Ship:
        """Test Ship
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Ship`
        """
        model = Ship()
        if include_optional:
            return Ship(
                symbol = '',
                registration = openapi_client.models.ship_registration.ShipRegistration(
                    name = '0', 
                    faction_symbol = '0', 
                    role = 'FABRICATOR', ),
                nav = openapi_client.models.ship_nav.ShipNav(
                    system_symbol = '0', 
                    waypoint_symbol = '0', 
                    route = openapi_client.models.ship_nav_route.ShipNavRoute(
                        destination = openapi_client.models.ship_nav_route_waypoint.ShipNavRouteWaypoint(
                            symbol = '0', 
                            type = 'PLANET', 
                            system_symbol = '0', 
                            x = 56, 
                            y = 56, ), 
                        origin = openapi_client.models.ship_nav_route_waypoint.ShipNavRouteWaypoint(
                            symbol = '0', 
                            type = 'PLANET', 
                            system_symbol = , 
                            x = 56, 
                            y = 56, ), 
                        departure_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        arrival = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    status = 'IN_TRANSIT', 
                    flight_mode = 'CRUISE', ),
                crew = openapi_client.models.ship_crew.ShipCrew(
                    current = 56, 
                    required = 56, 
                    capacity = 56, 
                    rotation = 'STRICT', 
                    morale = 0, 
                    wages = 0, ),
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
                cooldown = openapi_client.models.cooldown.Cooldown(
                    ship_symbol = '0', 
                    total_seconds = 0, 
                    remaining_seconds = 0, 
                    expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
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
                cargo = openapi_client.models.ship_cargo.ShipCargo(
                    capacity = 0, 
                    units = 0, 
                    inventory = [
                        openapi_client.models.ship_cargo_item.ShipCargoItem(
                            symbol = 'PRECIOUS_STONES', 
                            name = '', 
                            description = '', 
                            units = 1, )
                        ], ),
                fuel = openapi_client.models.ship_fuel.ShipFuel(
                    current = 0, 
                    capacity = 0, 
                    consumed = openapi_client.models.ship_fuel_consumed.ShipFuel_consumed(
                        amount = 0, 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
            )
        else:
            return Ship(
                symbol = '',
                registration = openapi_client.models.ship_registration.ShipRegistration(
                    name = '0', 
                    faction_symbol = '0', 
                    role = 'FABRICATOR', ),
                nav = openapi_client.models.ship_nav.ShipNav(
                    system_symbol = '0', 
                    waypoint_symbol = '0', 
                    route = openapi_client.models.ship_nav_route.ShipNavRoute(
                        destination = openapi_client.models.ship_nav_route_waypoint.ShipNavRouteWaypoint(
                            symbol = '0', 
                            type = 'PLANET', 
                            system_symbol = '0', 
                            x = 56, 
                            y = 56, ), 
                        origin = openapi_client.models.ship_nav_route_waypoint.ShipNavRouteWaypoint(
                            symbol = '0', 
                            type = 'PLANET', 
                            system_symbol = , 
                            x = 56, 
                            y = 56, ), 
                        departure_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        arrival = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    status = 'IN_TRANSIT', 
                    flight_mode = 'CRUISE', ),
                crew = openapi_client.models.ship_crew.ShipCrew(
                    current = 56, 
                    required = 56, 
                    capacity = 56, 
                    rotation = 'STRICT', 
                    morale = 0, 
                    wages = 0, ),
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
                cooldown = openapi_client.models.cooldown.Cooldown(
                    ship_symbol = '0', 
                    total_seconds = 0, 
                    remaining_seconds = 0, 
                    expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
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
                cargo = openapi_client.models.ship_cargo.ShipCargo(
                    capacity = 0, 
                    units = 0, 
                    inventory = [
                        openapi_client.models.ship_cargo_item.ShipCargoItem(
                            symbol = 'PRECIOUS_STONES', 
                            name = '', 
                            description = '', 
                            units = 1, )
                        ], ),
                fuel = openapi_client.models.ship_fuel.ShipFuel(
                    current = 0, 
                    capacity = 0, 
                    consumed = openapi_client.models.ship_fuel_consumed.ShipFuel_consumed(
                        amount = 0, 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), ),
        )
        """

    def testShip(self):
        """Test Ship"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
