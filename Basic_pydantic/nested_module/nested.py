from pydantic import BaseModel
from typing import List, Optional


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address


class Comment(BaseModel):
    comment_id: int
    content: str
    replies: Optional[List["Comment"]] = None


# Resolve the forward reference
Comment.model_rebuild()


# Create Address object
address = Address(
    street="Vishal Street",
    city="Bijnor, Uttar Pradesh",
    postal_code="10001",
)

# Create User object
user = User(
    id=1,
    name="Vishal",
    address=address,  # Pass the object, not the class
)

# Create nested comments
comments = Comment(
    comment_id=1,
    content="First comment",
    replies=[
        Comment(comment_id=2, content="Reply 1"),
        Comment(comment_id=3, content="Reply 2"),
    ],
)

print(user)
print("=======================\n")
print(comments)
