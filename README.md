# Convertly — Unit Converter

A small Python web app for converting length, mass, temperature, volume, and area.

## Open without localhost

To use the converter as a regular local webpage without starting Python, double-click `converter.html` in File Explorer. It opens directly in your browser and conversions work offline. Keep the `static` folder beside the HTML file so its styling loads.

## Run locally

1. Install Python 3.10 or newer.
2. In this folder, install the dependency:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Start the website:

   ```powershell
   python app.py
   ```

4. Open http://127.0.0.1:5000 in your browser.

## Run the unit tests

```powershell
python -m unittest discover -s tests
```
