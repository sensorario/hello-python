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


## Panoramica

In questo repository trovi un semplice esempio di applicazione desktop realizzata con PyQt5. Lo script serve a creare:

- **Finestra principale** (“Hello PyQt5”)
  - Quattro etichette (`QLabel`) posizionate verticalmente con testi di esempio (“Text 1” … “Text 4”).
  - Un pulsante **Quit** che chiude l’applicazione.
  - Un pulsante **Modale** che apre una finestra secondaria in modalità modale.

- **Finestra secondaria** (modal dialog)
  - Intitolata “Secondary Window”.
  - Contiene una singola etichetta che mostra il testo “This is the secondary window”.
  - Blocca l’interazione con la finestra principale finché non viene chiusa.

### Dipendenze

- Python 3.x
- PyQt5
