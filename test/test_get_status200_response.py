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

from openapi_client.models.get_status200_response import GetStatus200Response

class TestGetStatus200Response(unittest.TestCase):
    """GetStatus200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetStatus200Response:
        """Test GetStatus200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetStatus200Response`
        """
        model = GetStatus200Response()
        if include_optional:
            return GetStatus200Response(
                status = '',
                version = '',
                reset_date = '',
                description = '',
                stats = openapi_client.models.get_status_200_response_stats.get_status_200_response_stats(
                    agents = 56, 
                    ships = 56, 
                    systems = 56, 
                    waypoints = 56, ),
                leaderboards = openapi_client.models.get_status_200_response_leaderboards.get_status_200_response_leaderboards(
                    most_credits = [
                        openapi_client.models.get_status_200_response_leaderboards_most_credits_inner.get_status_200_response_leaderboards_mostCredits_inner(
                            agent_symbol = '', 
                            credits = 56, )
                        ], 
                    most_submitted_charts = [
                        openapi_client.models.get_status_200_response_leaderboards_most_submitted_charts_inner.get_status_200_response_leaderboards_mostSubmittedCharts_inner(
                            agent_symbol = '', 
                            chart_count = 56, )
                        ], ),
                server_resets = openapi_client.models.get_status_200_response_server_resets.get_status_200_response_serverResets(
                    next = '', 
                    frequency = '', ),
                announcements = [
                    openapi_client.models.get_status_200_response_announcements_inner.get_status_200_response_announcements_inner(
                        title = '', 
                        body = '', )
                    ],
                links = [
                    openapi_client.models.get_status_200_response_links_inner.get_status_200_response_links_inner(
                        name = '', 
                        url = '', )
                    ]
            )
        else:
            return GetStatus200Response(
                status = '',
                version = '',
                reset_date = '',
                description = '',
                stats = openapi_client.models.get_status_200_response_stats.get_status_200_response_stats(
                    agents = 56, 
                    ships = 56, 
                    systems = 56, 
                    waypoints = 56, ),
                leaderboards = openapi_client.models.get_status_200_response_leaderboards.get_status_200_response_leaderboards(
                    most_credits = [
                        openapi_client.models.get_status_200_response_leaderboards_most_credits_inner.get_status_200_response_leaderboards_mostCredits_inner(
                            agent_symbol = '', 
                            credits = 56, )
                        ], 
                    most_submitted_charts = [
                        openapi_client.models.get_status_200_response_leaderboards_most_submitted_charts_inner.get_status_200_response_leaderboards_mostSubmittedCharts_inner(
                            agent_symbol = '', 
                            chart_count = 56, )
                        ], ),
                server_resets = openapi_client.models.get_status_200_response_server_resets.get_status_200_response_serverResets(
                    next = '', 
                    frequency = '', ),
                announcements = [
                    openapi_client.models.get_status_200_response_announcements_inner.get_status_200_response_announcements_inner(
                        title = '', 
                        body = '', )
                    ],
                links = [
                    openapi_client.models.get_status_200_response_links_inner.get_status_200_response_links_inner(
                        name = '', 
                        url = '', )
                    ],
        )
        """

    def testGetStatus200Response(self):
        """Test GetStatus200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
