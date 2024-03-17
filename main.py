import app
import settings


def main() -> None:
    cols, data = app.query_from_redshift(
        app.QUERY,
        settings.REDSHIFT_HOST,
        settings.REDSHIFT_PORT,
        settings.REDSHIFT_DB,
        settings.REDSHIFT_USER,
        settings.REDSHIFT_PASSWORD
    )

    print(data)


if __name__ == '__main__':
    main()
