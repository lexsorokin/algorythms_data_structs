from collections import deque

def company_sells_product(company, key_word):
    if key_word in company.split(): 
        return True
    
def search(graph, start_company, product): 
    search_query = deque()
    search_query += graph[start_company]
    searched = []

    while search_query: 
        company = search_query.popleft()
        if company not in searched: 
            if company_sells_product(company, product):
                return f"Company {company} sells {product}"
            else: 
                search_query += graph[company]
                searched.append(company)


graph = {}
graph["One"] = ["Two", "Three", "Four"]
graph["Two"] = ["Three", "Five", "Six"]
graph["Three"] = ["Five", " Mango Seven", "Eight"]
graph["Four"] = []
graph["Five"] = []
graph["Six"] = ["Seven", "Eight", "Nine"]
graph["Seven"] = ["Eight", "Nine", "Ten"]

print(search(graph, "One", "Mango"))