# grocer-notifier

This app is an example project using the Grocer package.

It simply polls your grocer of choice and sends a text message to the number you provide if delivery times are available.

## To install:

```py
$ pip install git+https://github.com/itsjohnward/grocer-notifier
```

## To run:

1. Make sure you have a Twilio developer account set up, and then set your app keys:

```sh
$ export TWILIO_PHONE_NUMBER=+12345678910
$ export TWILIO_ACCOUNT_SID=putyourshere
$ export TWILIO_AUTH_TOKEN=putyourshere
```

2. Try running it:

```sh
$ grocerytime wegmans 1245678910
```

It should output a formatted message to the console. Once you're happy with how it's configured, you can turn on text messages by setting the following environment variable:

```
$ export TWILIO_PROD_MODE=TRUE
```