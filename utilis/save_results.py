import json

def save_to_json(parsed_paper, summary, filename="results.json"):
    """
    Save the parsed paper and summary to a JSON file.

    Args:
        parsed_paper (dict): The parsed paper data.
        summary (str): The summary of the paper.
        filename (str): The name of the file to save the results to.
    """
    results = {
        "title": parsed_paper["title"],
        "summary": summary
    }
    with open(filename, "a") as f:
        json.dump(results, f, indent=4)
        f.write("\n")
 