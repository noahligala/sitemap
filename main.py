import urllib.request
from html.parser import HTMLParser
import re

class SiteMapParser(HTMLParser):
    """Custom HTML parser to extract links from a web page."""
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':  # Extract links from anchor tags
            attrs = dict(attrs)
            link = attrs.get('href')
            if link:
                self.links.append(link)

def generate_site_map(url):
    """Generates the site map for the given URL."""
    try:
        # Fetch the web page content
        response = urllib.request.urlopen(url)
        html_content = response.read().decode('utf-8')

        # Parse the HTML content and extract links
        parser = SiteMapParser()
        parser.feed(html_content)
        links = parser.links

        # Print the site map
        print('Site Map for:', url)
        for link in links:
            print('- ', link)

    except Exception as e:
        print('Error generating site map:', e)

# Prompt user to enter a URL
url = input('Enter a URL to generate site map: ')

# Call the generate_site_map function with the user-inputted URL
generate_site_map(url)
