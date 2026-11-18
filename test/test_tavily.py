from tools.tavily_tool import tavily_search

res = tavily_search("Best travel destinations in Europe give me 3 best options with a brief description of each destination and why they are worth visiting.")
print(repr(res))