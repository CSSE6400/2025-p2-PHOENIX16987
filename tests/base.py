from todo import create_app
import unittest

class TodoTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_overrides={
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',  # 使用内存中的SQLite数据库
            'TESTING': True  # 启用测试模式
        })
        self.client = self.app.test_client()  # 创建一个测试客户端
    
    def assertDictSubset(self, expected_subset: dict, whole: dict):
        for key, value in expected_subset.items():
            self.assertEqual(whole[key], value)  # 比较字典的键值对

