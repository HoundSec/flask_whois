### Flask_Whois

![screely-1724513573716](https://github.com/user-attachments/assets/ffced920-f24e-417c-8737-b110ac185590)

![screely-1724513599255](https://github.com/user-attachments/assets/7c4cab38-f3fb-4657-88b2-6fafdb41568c)


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
- **`whois` command installed** on the system for domain lookup (see below for Docker support)
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

4. **Ensure `whois` is installed (if you're not using docker)**

   On Linux and macOS, you can install the `whois` command using your package manager.  
   - **Linux (Debian-based)**:  
     ```bash
     sudo apt-get install whois
     ```
   - **macOS (with Homebrew)**:  
     ```bash
     brew install whois
     ```

   On **Windows**, you will need to install `whois` manually, such as from [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/downloads/whois).

   **Note:** If the `whois` command is not available on your system, you can deploy and run the app using Docker.

### Usage

1. **Run the application**

   ```bash
   python app.py
   ```

2. **Access the app**

   Open your browser and navigate to `http://127.0.0.1:5000/`.

### Docker Support

Flask_Whois can be deployed using Docker, which comes pre-configured with the `whois` command to avoid system-specific installations.

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
   docker-compose up -d --build
   ```

2. **Access the app**

   Open your browser and navigate to `http://127.0.0.1:8000/`.

### Important Notes

- If you are not using Docker, ensure that the `whois` command is installed on your system to perform domain lookups.  
- For a smoother setup, consider using Docker, which includes the `whois` command in the container.

### Contributing

Contributions are welcome! Please open an issue to discuss your ideas or submit a pull request with your changes.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## About Me

I am Monazir Muhammad Doha, on a mission to bring my ideas to life.
Check my website [HoundSec](https://houndsec.net/)
