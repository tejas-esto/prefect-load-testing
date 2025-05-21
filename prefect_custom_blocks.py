from prefect.blocks.core import Block
from pydantic import SecretStr


class RedshiftCredentials(Block):
    """
    Custom block to store Redshift credentials

    Built as a replacement for the now deprecated DatabaseCredentials block in Prefect.

    This block is used only to store the credentials, the connections and cursors are created and managed using
    the official AWS Python package `redshift_connector`.

    Attributes:
        host (str): The host of the Redshift cluster
        port (int): The port of the Redshift cluster. Defaults to 5439
        database (str): The name of the database
        user (str): The username to connect to the database
        password (SecretStr): The password to connect to the database

    Example:
        ```python
        from prefect_custom_blocks import RedshiftCredentials
        import redshift_connector

        redshift_credentials = RedshiftCredentials.load("BLOCK_NAME")
        conn = redshift_connector.connect(
            host=redshift_credentials.host,
            port=redshift_credentials.port,
            database=redshift_credentials.database,
            user=redshift_credentials.user,
            password=redshift_credentials.password.get_secret_value()
        )
        ```
    """

    _logo_url = (
        "https://upload.wikimedia.org/wikipedia/commons/7/73/Amazon-Redshift-Logo.svg"
    )
    _block_type_name = "Redshift Credentials"

    host: str
    port: int = 5439
    database: str
    user: str
    password: SecretStr


# Register the block once
RedshiftCredentials.register_type_and_schema()
