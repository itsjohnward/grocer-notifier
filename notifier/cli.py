from grocer import GrocerClient
from twilio_utils import send


def main():
    parser = argparse.ArgumentParser(description="Pset 5")

    parser.add_argument("merchant", choices=["wegmans"])
    parser.add_argument(
        "phone",
        metavar="#",
        type=int,
        nargs=1,
        help="the phone number to send alerts to",
    )
    parser.add_argument("-e", "--email", action="store", type=str)
    parser.add_argument("-p", "--password", action="store", type=str)
    args = parser.parse_args()

    if len(str(args.phone)) != 11:
        raise ValueError(
            "Please enter a valid 11-digit phone number, including country code. i.e. 12223334444"
        )

    client = GrocerClient(args.merchant, args.email, args.password)

    previous_times = None
    while True:
        times = grocer.get_delivery_times(merchant=args["merchant"])
        # Send a message when availability changes:
        if len(times) > 0 and (previous_times is None or len(previous_times) == 0):
            send(
                number=args["phone"],
                message="\n".join([row for index, row in times.iterrows()]),
            )
        previous_times = times
