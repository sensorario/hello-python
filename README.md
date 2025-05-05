# Setting Up a Virtual Environment

To start a virtual environment for this project, follow these steps:

1. **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    ```

2. **Activate the Virtual Environment**:
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```

3. **Install Dependencies** (if any):
    ```bash
    pip install -r requirements.txt
    ```

4. **Deactivate the Virtual Environment** (when done):
    ```bash
    deactivate
    ```