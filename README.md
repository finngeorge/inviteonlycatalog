# Invite Only Catalog

Web application for centralizing artist and respective track data for clients of Invite Only Studios, NYC

## Getting Started

Create an `.env` file, get the environment variables from [some_secure_credentials_host - TBD](#) and put them in there

First, create a virtual environment and spin it up and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

Then, install necessary modules:

```bash
pip install -r requirements.txt
```

## Running Migrations

```bash
python manage.py migrate
```

## Running the Server

```bash
python manage.py runserver
```
