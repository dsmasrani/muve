from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from uber_rides.auth import AuthorizationCodeGrant


def main():
    auth_flow = AuthorizationCodeGrant('PtKMV4J2m6XTyaCq-9X2_QTTjGeC-rCO','request','P7anIftZUwq0rFDQn5zjxR0CZtsh4A4GEerABD4f')

    auth_url = auth_flow.get_authorization_url()

    session = Session(server_token=<TOKEN>)
    client = UberRidesClient(session)

    response = client.get_price_estimates(
        start_latitude=37.770,
        start_longitude=-122.411,
        end_latitude=37.791,
        end_longitude=-122.405,
        seat_count=2
    )

    estimate = response.json.get('prices')

    print(estimate)

