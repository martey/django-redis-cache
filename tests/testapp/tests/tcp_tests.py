# -*- coding: utf-8 -*-
from redis_cache.tests.testapp.tests.base_tests import BaseRedisTestCase
# from redis_cache.tests.testapp.tests.multi_server_tests import MultiServerTests
try:
    from django.test import override_settings
except ImportError:
    from django.test.utils import override_settings
from django.test import TestCase

from redis_cache.cache import ImproperlyConfigured
from redis.connection import UnixDomainSocketConnection


LOCATION = "127.0.0.1:6380"
LOCATIONS = [
    '127.0.0.1:6380',
    '127.0.0.1:6381',
    '127.0.0.1:6382',
]


class TCPTestCase(BaseRedisTestCase, TestCase):

    def test_bad_db_initialization(self):
        pass
        #self.assertRaises(ImproperlyConfigured, self.get_cache, 'redis_cache.cache://127.0.0.1:?db=not_a_number' % (server.host, server.port))

    def test_bad_port_initialization(self):
        pass
        #self.assertRaises(ImproperlyConfigured, self.get_cache, 'redis_cache.cache://%s:not_a_number?db=15' % server.host)

    def test_default_initialization(self):
        self.reset_pool()
        self.cache = self.get_cache()
        client = self.cache.clients[('127.0.0.1', 6380, 15, None)]
        connection_class = client.connection_pool.connection_class
        if connection_class is not UnixDomainSocketConnection:
            self.assertEqual(client.connection_pool.connection_kwargs['host'], '127.0.0.1')
            self.assertEqual(client.connection_pool.connection_kwargs['port'], 6380)
            self._skip_tearDown = True
        self.assertEqual(client.connection_pool.connection_kwargs['db'], 15)


# @override_settings(
#     CACHES={
#         'default': {
#             'BACKEND': 'redis_cache.RedisCache',
#             'LOCATION': LOCATION,
#             'OPTIONS': {
#                 'DB': 15,
#                 'PASSWORD': 'yadayada',
#                 'PARSER_CLASS': 'redis.connection.HiredisParser',
#                 'PICKLE_VERSION': 2,
#                 'CONNECTION_POOL_CLASS': 'redis.ConnectionPool',
#                 'CONNECTION_POOL_CLASS_KWARGS': {
#                     'max_connections': 2,
#                 }
#             },
#         },
#     }
# )
# class SingleHiredisTestCase(TCPTestCase):
#     pass


# @override_settings(
#     CACHES={
#         'default': {
#             'BACKEND': 'redis_cache.RedisCache',
#             'LOCATION': LOCATION,
#             'OPTIONS': {
#                 'DB': 15,
#                 'PASSWORD': 'yadayada',
#                 'PARSER_CLASS': 'redis.connection.PythonParser',
#                 'PICKLE_VERSION': 2,
#                 'CONNECTION_POOL_CLASS': 'redis.ConnectionPool',
#                 'CONNECTION_POOL_CLASS_KWARGS': {
#                     'max_connections': 2,
#                 }
#             },
#         },
#     }
# )
# class SinglePythonParserTestCase(TCPTestCase):
#     pass


# @override_settings(
#     CACHES={
#         'default': {
#             'BACKEND': 'redis_cache.ShardedRedisCache',
#             'LOCATION': LOCATIONS,
#             'OPTIONS': {
#                 'DB': 15,
#                 'PASSWORD': 'yadayada',
#                 'PARSER_CLASS': 'redis.connection.HiredisParser',
#                 'PICKLE_VERSION': 2,
#                 'CONNECTION_POOL_CLASS': 'redis.ConnectionPool',
#                 'CONNECTION_POOL_CLASS_KWARGS': {
#                     'max_connections': 2,
#                 }
#             },
#         },
#     }
# )
# class MultipleHiredisTestCase(MultiServerTests, TCPTestCase):
#     pass


# @override_settings(
#     CACHES={
#         'default': {
#             'BACKEND': 'redis_cache.ShardedRedisCache',
#             'LOCATION': LOCATIONS,
#             'OPTIONS': {
#                 'DB': 15,
#                 'PASSWORD': 'yadayada',
#                 'PARSER_CLASS': 'redis.connection.PythonParser',
#                 'PICKLE_VERSION': 2,
#                 'CONNECTION_POOL_CLASS': 'redis.ConnectionPool',
#                 'CONNECTION_POOL_CLASS_KWARGS': {
#                     'max_connections': 2,
#                 }
#             },
#         },
#     }
# )
# class MultiplePythonParserTestCase(MultiServerTests, TCPTestCase):
#     pass

