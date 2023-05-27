import unittest
import minium


class Mytest(minium.MiniTest):

    def test_view_products(self):
        url = '/pages/index/index'
        self.app.relaunch(url)
        text = self.page.get_element('text.item-title', text_contains='库洛米', max_timeout=3)  # 选择男士羽绒服
        text.click()
        self.page.wait_for('text.commodity-desc', max_timeout=3)
        text = self.page.get_element('text.commodity-desc')
        self.assertIn('库洛米', text.inner_text)

if __name__ == '__main__':
    unittest.main()  # 启动测试框架



    # def test_release(self):
    #     url = 'pages/publish/publish'
    #     self.app.relaunch(url)