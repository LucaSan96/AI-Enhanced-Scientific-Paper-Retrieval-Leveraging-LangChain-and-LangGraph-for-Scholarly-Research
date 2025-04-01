from search.arxiv import search_arxiv

def main():
    query = "Transformers in Natural Language Processing"  # Inserisci qui la tua query
    results = search_arxiv(query)

    if results:
        for idx, result in enumerate(results, 1):
            print(f"{idx}. {result['title']}")
            print(f"   Authors: {', '.join(result['authors'])}")
            print(f"   Published: {result['published']}")
            print(f"   Summary: {result['summary']}")
            print(f"   Link: {result['link']}")
            print("\n")
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
