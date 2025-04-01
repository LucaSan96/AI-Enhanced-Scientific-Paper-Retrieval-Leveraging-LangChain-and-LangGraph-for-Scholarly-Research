import  requests
from xml.etree import ElementTree as ET

# Search for papers on arXiv
def search_arxiv(query, max_results=5):
    """Search for papers on arXiv using a query string.
    
    Args:
        query (str): The search query string.
        max_results (int): The maximum number of results to return.
    
    Returns:
        list: A list of dictionaries containing paper information.
    """
    url = "http://export.arxiv.org/api/query?"
    search_url = f"{url}search_query={query}&start=0&max_results={max_results}&sortBy=relevance&sortOrder=descending"

    try:
        response = requests.get(search_url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the XML response
        root = ET.fromstring(response.content)

        papers = []
        for paper in root.findall('{http://www.w3.org/2005/Atom}entry'):
            title = paper.find('{http://www.w3.org/2005/Atom}title').text
            authors = [author.find('{http://www.w3.org/2005/Atom}name').text for author in paper.findall('{http://www.w3.org/2005/Atom}author')]
            published = paper.find('{http://www.w3.org/2005/Atom}published').text
            summary = paper.find('{http://www.w3.org/2005/Atom}summary').text
            link = paper.find('{http://www.w3.org/2005/Atom}link').attrib['href']
            
            papers.append({
                'title': title,
                'authors': authors,
                "published": published,
                'summary': summary,
                'link': link
            })
        
        return papers
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from arXiv: {e}")
        return []