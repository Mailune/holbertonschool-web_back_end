#!/usr/bin/env python3
"""NoSQL"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of all documents in the collection,
        or an empty list if the collection is empty.
    """
    documents = list(mongo_collection.find())

    return documents
