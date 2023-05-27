import unittest
import minium


class Mytest(minium.MiniTest):

    def test_log_in(self): #测试登录功能
        button_log_in = self.page.get_element('button.button-xy')  # 选择登录页面按钮
        button_log_in.click()
        self.assertEqual(self.page, "pages/index/index")

    def test_homepage_loading(self):
        url = '/pages/index/index'
        self.app.relaunch(url)
        self.assertEqual(True, self.page.element_is_exists('view.list-item', max_timeout=3))


if __name__ == '__main__':
    unittest.main()  # 启动测试框架
