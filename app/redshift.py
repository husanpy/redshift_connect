import redshift_connector


QUERY = """select *
from dbt_prod.fct_aggregated
limit 100"""


def query_from_redshift(query: str, host, port, db, user, pwd) -> tuple[list, tuple[list]]:
    """
    :param query: query to run against redshift
    :param host: redshift server host
    :param port: redshift server port
    :param db: redshift db name
    :param user: redshift user
    :param pwd: redshift user password
    :return: cols - list of columns' names in list, data - rows, tuples of lists
    """
    with redshift_connector.connect(
        host=host,
        port=port,
        database=db,
        user=user,
        password=pwd
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            cols = [d[0] for d in cursor.description]
            data = cursor.fetchall()
            return cols, data
