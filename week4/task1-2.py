from pathlib import Path
import sys
import collections
from collections import deque

class Wikipedia:

    # Initialize the graph of pages.
    def __init__(self, pages_file, links_file):

        # A mapping from a page ID (integer) to the page title.
        # For example, self.titles[1234] returns the title of the page whose
        # ID is 1234.
        self.titles = {}

        # A set of page links.
        # For example, self.links[1234] returns an array of page IDs linked
        # from the page whose ID is 1234.
        self.links = {}

        # Read the pages file into self.titles.
        with open(pages_file) as file:
            for line in file:
                (id, title) = line.rstrip().split(" ")
                id = int(id)
                assert not id in self.titles, id
                self.titles[id] = title
                self.links[id] = []
        print("Finished reading %s" % pages_file)

        # Read the links file into self.links.
        with open(links_file) as file:
            for line in file:
                (src, dst) = line.rstrip().split(" ")
                (src, dst) = (int(src), int(dst))
                assert src in self.titles, src
                assert dst in self.titles, dst
                self.links[src].append(dst)
        print("Finished reading %s" % links_file)
        print()


    # Find the longest titles. This is not related to a graph algorithm at all
    # though :)
    def find_longest_titles(self):
        titles = sorted(self.titles.values(), key=len, reverse=True)
        print("The longest titles are:")
        count = 0
        index = 0
        while count < 15 and index < len(titles):
            if titles[index].find("_") == -1:
                print(titles[index])
                count += 1
            index += 1
        print()


    # Find the most linked pages.
    def find_most_linked_pages(self):
        link_count = {}
        for id in self.titles.keys():
            link_count[id] = 0

        for id in self.titles.keys():
            for dst in self.links[id]:
                link_count[dst] += 1

        print("The most linked pages are:")
        link_count_max = max(link_count.values())
        for dst in link_count.keys():
            if link_count[dst] == link_count_max:
                print(self.titles[dst], link_count_max)
        print()


    # Find the shortest path.
    # |start|: The title of the start page.
    # |goal|: The title of the goal page.
    def find_shortest_path(self, start, goal):
        #------------------------#
        # Write your code here!  #
        #------------------------#
        
        # find id from titles 
        start_id = None
        goal_id = None
        for page_id, title in self.titles.items():
            if title == start:
                start_id = page_id
            elif title == goal:
                goal_id = page_id
            if start_id and goal_id:
                break
              
        if start_id is None or goal_id is None:
            print("Start or goal page not found")
            return None
        
        # BFS 
        # queue for remembering the neighbors
        queue = deque()
        queue.append(start_id)
        # history for remembering the distance and previous id 
        # to check shortest path and if visited
        history = {}  # id: (distance, previous id)
        history[start_id] = (0, None)

        while queue:
            current = queue.popleft()
            distance, prev = history[current]

            if current == goal_id:
                path = []
                while current is not None:
                    path.append(self.titles[current])
                    current = history[current][1]
                path.reverse()
                print(path)
                return 

            for neighbor in self.links[current]:
                if neighbor not in history:
                    queue.append(neighbor)
                    history[neighbor] = (distance + 1, current)
                elif distance + 1 < history[neighbor][0]:
                    history[neighbor] = (distance + 1, current)

        print("no path found")
        return None
        
                


    def calculate_page_rank(self):
        # Initialize page scores
        scores = {id: 1.0 for id in self.titles.keys()}
        
        total_nodes = len(scores)
        main_rate = 0.85
        convergence_threshold = 0.01
        iteration_limit = 100
        totalSum =total_nodes *1.0
        delta = 0.0

        for iteration in range(iteration_limit):
            new_scores = {id: 0.0 for id in self.titles.keys()}
            total_score = 0.0

            for id in self.titles.keys():
                outgoing_links = self.links.get(id, [])  # 出リンク

            
                score_forall = 0.0

                if len(outgoing_links) == 0:
                    score_forall = main_rate * scores[id] / total_nodes
                else:
                    adjusted_score = scores[id]* main_rate / len(outgoing_links) 
                    for dst_id in outgoing_links:
                        new_scores[dst_id] += adjusted_score
                    score_forall = scores[id] *(1-main_rate) / total_nodes
                    
            for id in self.titles.keys():
                new_scores[id] += score_forall
                total_score += new_scores[id]
                delta += abs(scores[id] - new_scores[id])
            

            #収束
            if abs(delta) < convergence_threshold:
                break
            
            scores = new_scores.copy()

        return scores

    def find_most_popular_pages(self):
        page_ranks = self.calculate_page_rank()

        # Sort the pages by their page rank in descending order
        sorted_pages = sorted(page_ranks.items(), key=lambda x: x[1], reverse=True)

        # Print the top 10 pages
        for i, (page_id, rank) in enumerate(sorted_pages[:10]):
            page_title = self.titles[page_id]
            print(f"Rank {i+1}: {page_title} (Page ID: {page_id}, Page Rank: {rank: .10f})")


            
        
        
            


    # Do something more interesting!!
    def find_something_more_interesting(self):
        #------------------------#
        # Write your code here!  #
        #------------------------#
        pass


if __name__ == "__main__":
    # if len(sys.argv) != 3:
    #     print("usage: %s pages_file links_file" % sys.argv[0])
    #     exit(1)

    # wikipedia = Wikipedia(sys.argv[1], sys.argv[2])
    filesize = "small"
    
    dir = Path(sys.argv[0]).parent.absolute()
    pages_file = Path.joinpath(dir, "wikipedia_dataset", f"pages_{filesize}.txt")
    links_file = Path.joinpath(dir, "wikipedia_dataset", f"links_{filesize}.txt")
    wikipedia = Wikipedia(pages_file, links_file)
    wikipedia.find_longest_titles()
    wikipedia.find_most_linked_pages()
    # wikipedia.find_shortest_path("渋谷", "小野妹子")
    wikipedia.find_shortest_path('A', 'E')
    wikipedia.find_most_popular_pages()
    