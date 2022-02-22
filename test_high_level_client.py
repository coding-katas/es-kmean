import unittest
from low_level_client_by_connection import ESLowLevelClientByConnection
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import Q, MatchPhrase



class TestHighLevelClientSearch(unittest.TestCase):

    def test_match_phrase_query_via_low_level_client(self):
        # call the query method
        search = Search(index='books', using=ESLowLevelClientByConnection.get_instance()).query(
            'match_phrase', synopsis='Java Concurrency in Practice')
        response = search.execute()
        self.assertEqual(response['hits']['total']['value'], 1)
        print(response.to_dict())

    def test_match_phrase_query_via_connection(self):
        ESLowLevelClientByConnection.get_instance()
        search = Search(index='books', using='high_level_client')
        # call the Q method
        search.query = Q('match_phrase', synopsis='Java Concurrency in Practice')
        response = search.execute()
        self.assertEqual(response['hits']['total']['value'], 1)

    def test_match_phrase_class_via_connection(self):
        ESLowLevelClientByConnection.get_instance()
        # construct the query object using the class of the query type
        search = Search(index='books', using='high_level_client')
        search.query = MatchPhrase(synopsis='Java Concurrency in Practice')
        response = search.execute()
        self.assertEqual(response['hits']['total']['value'], 1)
