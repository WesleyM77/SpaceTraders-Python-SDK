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

from openapi_client.models.deliver_contract200_response_data import DeliverContract200ResponseData

class TestDeliverContract200ResponseData(unittest.TestCase):
    """DeliverContract200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeliverContract200ResponseData:
        """Test DeliverContract200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeliverContract200ResponseData`
        """
        model = DeliverContract200ResponseData()
        if include_optional:
            return DeliverContract200ResponseData(
                contract = openapi_client.models.contract.Contract(
                    id = '0', 
                    faction_symbol = '0', 
                    type = 'PROCUREMENT', 
                    terms = openapi_client.models.contract_terms.ContractTerms(
                        deadline = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        payment = openapi_client.models.contract_payment.ContractPayment(
                            on_accepted = 56, 
                            on_fulfilled = 56, ), 
                        deliver = [
                            openapi_client.models.contract_deliver_good.ContractDeliverGood(
                                trade_symbol = '0', 
                                destination_symbol = '0', 
                                units_required = 56, 
                                units_fulfilled = 56, )
                            ], ), 
                    accepted = True, 
                    fulfilled = True, 
                    expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deadline_to_accept = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                cargo = openapi_client.models.ship_cargo.ShipCargo(
                    capacity = 0, 
                    units = 0, 
                    inventory = [
                        openapi_client.models.ship_cargo_item.ShipCargoItem(
                            symbol = 'PRECIOUS_STONES', 
                            name = '', 
                            description = '', 
                            units = 1, )
                        ], )
            )
        else:
            return DeliverContract200ResponseData(
                contract = openapi_client.models.contract.Contract(
                    id = '0', 
                    faction_symbol = '0', 
                    type = 'PROCUREMENT', 
                    terms = openapi_client.models.contract_terms.ContractTerms(
                        deadline = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        payment = openapi_client.models.contract_payment.ContractPayment(
                            on_accepted = 56, 
                            on_fulfilled = 56, ), 
                        deliver = [
                            openapi_client.models.contract_deliver_good.ContractDeliverGood(
                                trade_symbol = '0', 
                                destination_symbol = '0', 
                                units_required = 56, 
                                units_fulfilled = 56, )
                            ], ), 
                    accepted = True, 
                    fulfilled = True, 
                    expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deadline_to_accept = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
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
        )
        """

    def testDeliverContract200ResponseData(self):
        """Test DeliverContract200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
