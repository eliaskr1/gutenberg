from urllib import request
import pandas as pd
import json
import ssl

def json_data_to_html_table(api_url, columns=None):
    '''Konverterar json data från api till en
    html tabell med Pandas'''

    context = ssl._create_unverified_context()
    try:
        json_data = request.urlopen(api_url, context=context).read()
        data = json.loads(json_data)

        # Försök om det finns resultat (böcker)
        try:
            if 'results' in data:
                df = pd.DataFrame(data['results'])

                # ni kan lägga till fler om ni vill
                df = df[['title', 'authors', 'subjects', 'languages']]

                # Formatera authors så man får endast namn
                df['authors'] = df['authors'].apply(lambda authors: authors[0]['name'] if authors else 'No Author')

                if columns == None:
                    table_data = df.to_html(classes="table p-5", justify="left")
                else:
                    table_data = df.to_html(columns=columns, classes="table p-5", justify="left")

                return table_data
        # Om det inte finns resultat för användarens parametrar
        except:
            return "No results (books) were found with the desired inputs"
    except Exception as e:
        return e