import blpapi

class BLPRefSession():
    """XXX need to later decide how to create access to bbrg data
    Do we want single session that is on?  Possible multiple session instantiations?
    redo for use as context manager?
    """

    def __init__(self):
        # Fill SessionOptions
        sessionOptions = blpapi.SessionOptions()
        sessionOptions.setServerHost("localhost")
        sessionOptions.setServerPort(8194)

        # Create a Session
        self.session = blpapi.Session(sessionOptions)

    def start(self):
        # Start a Session
        if not self.session.start():
            print("Failed to start session.")
            return

        if not self.session.openService("//blp/refdata"):
            print("Failed to open //blp/refdata")
            return

        self.refDataService = self.session.getService("//blp/refdata")

    def get_price(self, ticker):
        """Pass an iterable of bloomberg tickers
        """
        request = self.refDataService.createRequest("ReferenceDataRequest")
        # append securities to request
        for t in ticker:
            print("Ticker:", t)
            request.append("securities", t)

        #  append fields to request
        request.append("fields", "PX_LAST")
        #request.append("fields", "DS002")

        print("Sending Request:", request)
        self.session.sendRequest(request)

        # Process received events
        while(True):
            # We provide timeout to give the chance to Ctrl+C handling:
            ev = self.session.nextEvent(500)
            for msg in ev:
                print("Message...")
                print("--- correlationIds")
                print(msg.correlationIds())
                print("--- asElement")
                print(msg.asElement())
                print("--- element name")
                print(msg.asElement().name())
                print("--- numElements")
                print(msg.numElements())
                print("--- messageType")
                print(msg.messageType())
                print("---")
                print(msg)


            # Response completly received, so we could exit
            if ev.eventType() == blpapi.Event.RESPONSE:
                print("---2 getElement")
                elist = msg.getElement("securityData")
                for i,e in enumerate(elist.values()):
                    sube = e.getElement("fieldData").getElement("PX_LAST")
                    print("{}-{}".format(i, sube))
                break

# Stop the session
#self.session.stop()

def main():
    mysession = BLPRefSession()
    print("here1")
    mysession.start()
    print("here2")
    mysession.start()
    print("here3")
    print(mysession.get_price(["UUP 05/04/18 C24 Equity"]))
    print(mysession.get_price(["AMZN Equity", "MU Equity"]))

if __name__ == "__main__":
    print("Testing...")
    try:
        main()
    except KeyboardInterrupt:
        print("Ctrl+C pressed. Stopping...")