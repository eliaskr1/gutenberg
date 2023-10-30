from urllib import request
import pandas as pd
from urllib import error
import json
import ssl

def json_data_to_html_table(api_url, columns=None):
    '''Konverterar json data från api till en
    html tabell med Pandas'''

    context = ssl._create_unverified_context()
    try:
        json_data = request.urlopen(api_url, context=context).read()
        data = json.loads(json_data)
        df = pd.DataFrame(data)

        if columns==None:
            table_data = df.to_html(classes="table p-5", justify="left")    
        else:
            table_data = df.to_html(columns=columns,classes="table p-5", justify="left")

        return table_data
    except Exception as e:
        # Om man försöker ladda elpriser som inte har publicerats ännu.
        if isinstance(e, error.HTTPError) and e.code == 404:
            return "Sidan existerar inte."

        # Plats för annan eventuell felhantering
        return "Ett fel uppstod. Kontakta administratören för hjälp."