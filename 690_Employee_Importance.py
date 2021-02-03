"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res = 0
        emp_map = {}
        for emp in employees:
            emp_map[emp.id] = emp

        emp = emp_map[id]
        q = deque([emp])
        sum = 0
        while len(q):
            node = q.popleft()
            sum += node.importance
            for i in node.subordinates:
                if i:
                    q.append(emp_map[i])

        return sum