
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {"first_name": "John", "last_name": self.last_name, "id": 1, "age": 33, "lucky_numbers": [7, 13, 22]},
            {"first_name": "Jane", "last_name": self.last_name, "id": 2, "age": 35, "lucky_numbers": [10, 14, 3]},
            {"first_name": "Jimmy", "last_name": self.last_name, "id": 3, "age": 5, "lucky_numbers": [1]}
        ]
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        print("ADDING MEMBER TEST", member["id"], isinstance(member["id"], int))
        try:
            if isinstance(member["id"], int):
                member_id = member["id"]
            else:
                member_id = self._generateId()
        except:
            member_id = self._generateId()

        print("PRINTING")

        new_member = {
            "id": member_id,
            "first_name": member["first_name"],
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        }
        self._members.append(new_member)
       
    def delete_member(self, id):
        # fill this method and update the return
        inital_len = len(self._members)
        pos = None
        for i, member in enumerate(self._members):
            print(i, member)
            if member["id"] == id:
                pos = i
        self._members.pop(pos)
        return len(self._members) < inital_len

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            print("PRINTING", member)
            if member["id"] == id:
                return member
        return False

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
