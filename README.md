# Redshift connector

Connect to redshift and query datasets.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/husanpy/redshift_connect.git
   ```

## Configuration

1. Create a `.env` file in the project root directory.
2. Add the following configuration parameters to the `.env` file:

    ```text
   REDSHIFT_HOST=your_redshift_host
   REDSHIFT_PORT=your_redshift_port
   REDSHIFT_DB=your_redshift_db_name
   REDSHIFT_USER=your_redshift_user
   REDSHIFT_PASSWORD=your_redshift_password
   ```
   
## Usage

1. Build the Docker image:

   ```bash
   docker build -t my-app .
   ```
   
2. Run the Docker container:

    ```bash
   docker run --env-file .env my-app
   ```
   
## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
