# epsonprinter-api
This package can be used to scrape the ink levels from your Epson Workforce printer.
## Usage:

### Connection
Create the API object with the IP address of the printer, on connect the values are fetched from the printer.
The protocol can be http or https. The default is http.
We can verify (or not) the ssl certificate chain if the protocol is not http if we define the verify_ssl paramter.
```python
api = EpsonPrinterAPI(<IP>, [[protocol={"http"|"https"}, [verify_ssl={False|True}]])
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


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Below are a list of resources that I used to assist with this project.

* This api wouldn't exist without the original author [ThaStealth](https://github.com/thastealth)
