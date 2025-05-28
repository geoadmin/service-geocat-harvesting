# 🚀 Getting Started

## Installation

=== "Basic install"

    ```sh
    pip install requests python-dotenv
    git clone https://github.com/geoadmin/service-geocat-harvesting
    # Installation complete
    ```

=== "Adapt proxies"

    ```sh
    & "C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\Scripts\pip3" install --proxy=proxy-bvcol.admin.ch:8080 requests python-dotenv
    ```

## Configuration

1. Create `.env` file:

    ```sh
    cp .env.example .env
    nano .env
    ```

2. Edit `config.py`:

    ```python
    # Target group ID
    PARAMETER_GROUP = 42  # (1)
    
    # Update dateStamp after upload?
    UPDATE_DATE_STAMP = True
    ```

    1. Change to your target group ID

## First Run

```sh
python main.py
# [INFO] Uploaded 5 files successfully
```