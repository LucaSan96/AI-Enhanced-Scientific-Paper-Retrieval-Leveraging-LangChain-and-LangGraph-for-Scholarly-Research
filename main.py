from search.search_arxiv import search_arxiv
from processing.parser import parse_paper
from processing.summarizer import summarize_paper
from utilis.save_results import save_to_json
from utilis.logger import setup_logger

def main():
    # Setup logger
    logger = setup_logger()
    logger.info("Starting the AI Research Assistant.")

    # Search for papers on arXiv
    query = input("Enter your search query: ")

    logger.info(f"Searching for papers with query: {query}")
    papers = search_arxiv(query)

    # Check if papers were found
    if not papers:
        logger.warning("No papers found for the given query.")
        return
    
    #Parse and summarize papers
    for paper in papers:
        logger.info(f"Parsing paper: {paper['title']}")
        parsed_paper = parse_paper(paper)
        
        logger.info(f"Summarizing paper: {parsed_paper['title']}")
        summary = summarize_paper(parsed_paper)
        
        # Save the results
        save_to_json(parsed_paper, summary)
        logger.info(f"Saved results for paper: {parsed_paper['title']}")

if __name__ == "__main__":
    main()