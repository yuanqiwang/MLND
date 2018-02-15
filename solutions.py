"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring of s.
For example: if s = "udacity" and t = "ad", then the function returns True.
Your function definition should look like: question1(s, t) and return a boolean True or False.
"""
def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def question1(s, t):
    # deal with edge cases for s and t
    if s == None or t == None or not t or isinstance(s, str) == False or isinstance(t, str) == False:
        return "Warning: input is incorrect"
    else:
        for i in range(0, len(s) - len(t) + 1):
            test = s[i:i + len(t)]
            if is_anagram(test, t):
                return True
        return False


def test1():
    print("\nTesting 1")
    print("Edge case (empty string):", "Pass" if question1("","") == "Warning: input is incorrect" else "Fail")
    print("Edge case (not a string):", "Pass" if question1(0, ['Udacity']) == "Warning: input is incorrect" else "Fail")
    print("Case 1:", "Pass" if question1("Udacity", "owl")== False else "Fail")
    print("Case 2:", "Pass" if question1("Udacity","ud") == True else "Fail")
    print("Case 3:", "Pass" if question1("Udacity","Udacityzb")== False else "Fail")


test1()


"""
Question 2
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.
"""


def is_palindromic(s):
    """
    check if the word is a palindromic
    """
    s = s.lower()
    half = int(len(s)/2)
    if s[:len(s)-half] == s[half:][::-1]:
        return s


def question2(a):
    # check inputs is a string:
    if not isinstance(a, str):
        return "Warning: input is not a string"
    else:
        for i in range(1,len(a)):
            window = len(a)-i+1
            for j in range(0,i):
                s = a[j: window + j]
                if is_palindromic(s):
                    return s


def test2():
    a1 = "isnotpalindromic"
    a2 = ""
    a3 = 1
    a4 = "abba"
    a5 = "zabcacbajz"

    print("\nTesting 2")
    print("Edge case (empty string):", "Pass" if question2(a2) == None else "Fail")
    print("Edge case (not a string):", "Pass" if question2(a3) == "Warning: input is not a string" else "Fail")
    print("Case 1:", "Pass" if question2(a1) == None else "Fail")
    print("Case 2:", "Pass" if question2(a4) == 'abba' else "Fail")
    print("Case 3:", "Pass" if question2(a5) == 'abcacba' else "Fail")


test2()


"""
Given an undirected graph G, find the minimum spanning tree within G.
A minimum spanning tree connects all vertices in a graph with the smallest
possible total weight of edges. Your function should take in
and return an adjacency list structured like this:
{'A':[('B',2)],'B':[('A',2),('C',5)],'C':[('B',5)]}.
Vertices are represented as unique strings.
The function definition should be "question3(G)"
"""


def question3(G):
    # implementation of Kruskal's algorithm

    # check if G is dictionary
    if type(G) != dict:
        return "Warning: input is not dictionary"

    # check if G have more than one node
    if len(G) < 2:
        return "Warning: input does not have enough vertices to form edges"

    # create a vertices list
    vertices = G.keys()

    # get unique set of edges
    edges = set()
    for i in vertices:
        for j in G[i]:
            if i > j[0]:
                edges.add((j[1], j[0], i))
            elif i < j[0]:
                edges.add((j[1], i, j[0]))

    # sort edges by weight
    edges = sorted(list(edges))

    # loop through edges and store only the needed ones
    output_edges = []
    vertices = [set(i) for i in vertices]
    for i in edges:
        # get indices of both vertices
        for j in range(len(vertices)):
            if i[1] in vertices[j]:
                i1 = j
            if i[2] in vertices[j]:
                i2 = j

        # store union in the smaller index and pop the larger index
        # also store the edge in output_edges
        if i1 < i2:
            vertices[i1] = set.union(vertices[i1], vertices[i2])
            vertices.pop(i2)
            output_edges.append(i)

    # generate the ouput graph from output_edges
    output_graph = {}
    for i in output_edges:
        if i[1] in output_graph:
            output_graph[i[1]].append((i[2], i[0]))
        else:
            output_graph[i[1]] = [(i[2], i[0])]

        if i[2] in output_graph:
            output_graph[i[2]].append((i[1], i[0]))
        else:
            output_graph[i[2]] = [(i[1], i[0])]
    return output_graph


def test3():
    print("\nTesting 3")
    print("Edge case (not dictionary):",
          "Pass" if "Warning: input is not dictionary" == question3(123) else "Fail")
    print("Edge case (empty dictionary):",
          "Pass" if "Warning: input does not have enough vertices to form edges" == question3({}) else "Fail")
    G = {'A': [('B', 2)],
         'B': [('A', 2), ('C', 5)],
         'C': [('B', 5)]}
    print("Case 1:", "Pass" if G == question3(G) else "Fail")
    G = {'A': [('B', 7), ('D', 5)],
         'B': [('A', 7), ('D', 9), ('C', 8), ('E', 7)],
         'C': [('B', 8), ('E', 5)],
         'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
         'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
         'F': [('D', 6), ('E', 8), ('G', 11)],
         'G': [('E', 9), ('F', 11)]}
    H = {'A': [('D', 5), ('B', 7)],
         'B': [('A', 7), ('E', 7)],
         'C': [('E', 5)],
         'D': [('A', 5), ('F', 6)],
         'E': [('C', 5), ('B', 7), ('G', 9)],
         'F': [('D', 6)],
         'G': [('E', 9)]}
    print("Case 2:", "Pass" if H == question3(G) else "Fail")


test3()


"""
Find the least common ancestor between two nodes on a binary search tree.
The least common ancestor is the farthest node from the root that is an ancestor
of both nodes. For example, the root is a common ancestor of all nodes on the
tree, but if both nodes are descendents of the root's left child, then that left
child might be the lowest common ancestor. You can assume that both nodes are in
the tree, and the tree itself adheres to all BST properties. The function
definition should look like question4(T, r, n1, n2), where Tis the tree
represented as a matrix, where the index of the list is equal to the integer
stored in that node and a 1 represents a child node, r is a non-negative integer
representing the root, and n1 and n2 are non-negative integers representing the
two nodes in no particular order. For example, one test case might be ...
question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
"""


def parent(T, n):
    # return parent of n if it exists, return None otherwise
    numrows = len(T)
    for i in range(numrows):
        if T[i][n] == 1:
            return i
    return None


def question4(T, r, n1, n2):
    # deal with invalid input T
    if not isinstance(T, list) or len(T) == 0 or len(T[0]) == 0:
        return "Warning: input is invalid"

    # deal with invalid input n1 and n2
    if n1 >= len(T) or n2 >= len(T):
        return "Warning: input n1 or n2 is invalid"

    # find all parents of n1
    n1_parent = []
    while n1 != r:
        n1 = parent(T, n1)
        n1_parent.append(n1)
    if len(n1_parent) == 0:
        return None
    while n2 != r:
        n2 = parent(T, n2)
        if n2 in n1_parent:
            return n2
    return None


def test4():
    print("\nTesting 4")
    print("Case 1:", "Pass"
          if question4([[0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0]], 3, 1, 4) == 3 else "Fail")

    print("Case 2:", "Pass"
           if question4([[0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 1, 0, 0, 0, 1],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 1, 1, 0, 0],
                         [0, 0, 0, 0, 0, 0]], 4, 1, 5) == 2 else "Fail")

    print("Edge case:", "Pass" if question4([], 4, 1, 5) == "Warning: input is invalid" else "Fail")


test4()

"""
Question 5
Find the element in a singly linked list that's m elements from the end.
For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element.
The function definition should look like question5(ll, m),
where ll is the first node of a linked list and m is the "mth number from the end".
You should copy/paste the Node class below to use as a representation of a node in the linked list.
Return the value of the node at that position.
"""


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


def question5(ll, m):
    if not ll:
        return None

    # get total length of the linked list
    current = ll
    total = 0
    while current is not None:
        current = current.next
        total += 1

    if m > total:
        return None

    # go to the mth place one step at a time
    goal = total - m
    current = ll
    step = 0
    while current is not None and step < goal:
        current = current.next
        step += 1
    return current.data


def test5():
    print("\nTesting 5")
    x1 = Node(1)
    x1.next = Node(2)
    x1.next.next = Node(3)
    x1.next.next.next = Node(4)
    x1.next.next.next.next = Node(5)
    x1.next.next.next.next.next = Node(6)
    print("Case 1:", "Pass" if question5(x1, 2) == 5 else "Fail")
    print("Case 2:", "Pass" if question5(x1, 3) == 4 else "Fail")
    print("Edge Case:", "Pass" if question5("", 4) == None else "Fail")
    print("Edge Case:", "Pass" if question5(x1, 9) == None else "Fail")


test5()
