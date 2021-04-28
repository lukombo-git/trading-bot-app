import logging

from connectors.binance_futures import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("3d42470c41be30e86f59aea3c200074f6cb5d70819c911f863f162dcdf337705",
                            "15d30ca5d335b7ac29d24bdd8ae4e7bec78440c70445a3b77a50bde56693179e",
                            testnet=True, futures=True)
    bitmex = BitmexClient("pYUdy18I1np1eiFUOvIUPTVE", "JuLyq1zHClikOeHWxMuoT-osMsU9qu2DiPDXF0WzRVnEYCEx", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
