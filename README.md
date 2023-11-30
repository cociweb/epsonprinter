# epsonprinter-api
This package can be used to scrape the ink levels from your Epson Workforce printer.
## Usage:

### Connection
Create the API object with the IP address of the printer, on connect the values are fetched from the printer
```python
api = EpsonPrinterAPI(<IP>)
```

Fetches the latest values from the printer
### Update values
```python
api.update()
```
### Get actual values
```python
#regular colours
photoblack = api.getSensorValue("photoblack")
black = api.getSensorValue("black")
magenta = api.getSensorValue("magenta")
cyan = api.getSensorValue("cyan")
yellow = api.getSensorValue("yellow")

# Cleaning cardridge
clean = api.getSensorValue("clean")
```

