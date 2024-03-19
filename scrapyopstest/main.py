import requests

response = requests.get(
  url='https://proxy.scrapeops.io/v1/',
  params={
      'api_key': '748837e3-9080-420f-b8cb-40fd7633145d',
      'url': 'https://quotes.toscrape.com/', 
      'render_js': 'true', 
      'residential': 'true', 
      'country': 'us', 
  },
)

print('Response Body: ', response.request.url)