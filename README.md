### Flask_Whois

# Flask_Whois

Flask_Whois is a web application that allows you to look up domain names and IP addresses, providing detailed WHOIS information, including expiration dates and raw data.

## Features

- **Domain/IP Lookup**: Enter a domain or IP address to fetch its WHOIS information.
- **Formatted Dates**: Expiration dates are displayed with ordinal indicators for enhanced readability.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Python `whois` package
- Docker (for containerized deployment)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/flask_whois.git
   cd flask_whois
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Run the application**

   ```bash
   python app.py
   ```

2. **Access the app**

   Open your browser and navigate to `http://127.0.0.1:5000/`.

### Docker Support

Flask_Whois can be deployed using Docker for ease of setup and scalability.

1. **Build the Docker image**

   ```bash
   docker build -t flask_whois .
   ```

2. **Run the Docker container**

   ```bash
   docker run -p 8000:8000 flask_whois
   ```

3. **Access the app**

   Open your browser and navigate to `http://127.0.0.1:8000/`.

### Docker Compose

To run the application using Docker Compose, use the following `docker-compose.yml`:

```yaml
services:
  flask_whois:
    build: .
    ports:
      - "8000:8000"
    restart: always
```

1. **Run the application with Docker Compose**

   ```bash
   docker-compose up -d
   ```

2. **Access the app**

   Open your browser and navigate to `http://127.0.0.1:8000/`.

### Contributing

Contributions are welcome! Please open an issue to discuss your ideas or submit a pull request with your changes.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## About Me

I’m Monazir Muhammad Doha. I am on a mission to bring his ideas to life.
Check my website [HoundSec](https://houndsec.net/)
