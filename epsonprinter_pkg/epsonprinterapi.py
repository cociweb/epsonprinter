import urllib.request
from bs4 import BeautifulSoup

class EpsonPrinterAPI(object):
    def __init__(self, ip):
        """Initialize the link to the printer status page."""
        self._resource = "http://" + ip + "/PRESENTATION/HTML/TOP/PRTINFO.HTML"
        self.available = True
        self.soup = None
        self.update()

    def getSensorValue(self, sensor):
        """To make it the user easier to configure the cartridge type."""
        if sensor == "black":
            sensorCorrected = "BK"
        elif sensor == "photoblack":
            sensorCorrected = "PB"
        elif sensor == "magenta":
            sensorCorrected = "M"
        elif sensor == "cyan":
            sensorCorrected = "C"
        elif sensor == "yellow":
            sensorCorrected = "Y"
        elif sensor == "clean":
            sensorCorrected = "Waste"
        else:
            return 0;

        try:
            for li in self.soup.find_all("li", class_="tank"):
                if sensorCorrected == "Waste":
                    div = li.find("div", class_="mbicn")
                else:
                    div = li.find("div", class_="clrname")

                if div != None and (div.contents[0] == sensorCorrected or sensorCorrected == "Waste"):
                    return int(li.find("div", class_="tank").findChild()["height"]) * 2
        except Exception as e:
            return 0


    def get_mac(self):
        """Get the mac of the printer."""
        try:
            for tr in self.soup.find_all("tr", class_="item-last clearfix"):
                mac = tr.find("td", class_="item-value")
                
                if mac != None:
                    return mac.get_text()
        except:
            return None

    def update(self):
        try:
            """Just fetch the HTML page."""
            response = urllib.request.urlopen(self._resource)
            data = response.read()
            response.close()

            self.soup = BeautifulSoup(data, "html.parser")
            self.available = True
        except Exception as e:
            self.available = False



