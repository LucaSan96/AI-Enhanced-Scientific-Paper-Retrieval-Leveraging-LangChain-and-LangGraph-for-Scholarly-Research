def parse_paper(paper):
   """Parse the content of a paper and extract relevant information."""
   
   parsed_data = {
        "title": paper["title"],
        "summary": paper["summary"],
    }
   
   return parsed_data
