import unittest
import minium


class Mytest(minium.MiniTest):

    def test_comment(self):
        url = '/pages/index/index'
        self.app.relaunch(url)
        text = self.page.get_element('text.item-title', text_contains='Apple', max_timeout=3)  # 选择商品
        text.click()
        input = self.page.get_element('input.comment-input')
        input.input("我认为这部手机很值")
        button = self.page.get_element('button.input-button')
        button.click()
        self.assertEqual(True, self.page.element_is_exists('text.comment-text', text_contains="我认为这部手机很值", max_timeout=3))

if __name__ == '__main__':
    unittest.main()  # 启动测试框架
