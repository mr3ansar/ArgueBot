import requests

secrets.API_KEY = "AIzaSyAG68uhc_QDrtu124I4btonmsgRc-rj1pg"
secrets.CX = "Search_id"

def search_web(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch results. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error during search: {e}")
        return None

def filter_results(results):
    trusted_domains = ["gov", "edu", "nytimes.com", "bbc.com", "wikipedia.org"]
    filtered_results = []
    if results and "items" in results:
        for item in results["items"]:
            domain = item["link"].split("/")[2]
            if any(trusted in domain for trusted in trusted_domains):
                filtered_results.append(item)
    return filtered_results
